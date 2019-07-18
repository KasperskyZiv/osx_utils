#!/usr/bin/env python3
# Created by Ziv Kaspersky <ziv.k@airoav.com> at 2019-07-16
#     ____    _      ____     ____ _    __
#    /    |  (_)____/ __ \   /    | |  / /
#   / /_| | / / ___/ / / /  / /_| | | / /
#  / ___  |/ / /  / /_/ /  / ___  | |/ /
# /_/   |_/_/_/   \____/  /_/   |_|___/

# Standard packages
import json
import logging
import os
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Any
import plistlib

# Proprietary packages
from binary_parser import BinaryParser
from dictionaries import entry_type_translation
from utils import _slugify, is_dmg, calc_hashes

logger = logging.getLogger(__name__)


class DMGUtilsError(Exception):
    pass


@dataclass()
class Block:
    """ base class for object parsed from file """
    file_path: str = field(repr=False)
    offset: int = field()


@dataclass()
class KolyBlock(Block):
    """ The main header for a DMG file"""
    # koly fields:
    # =============

    Signature: str = field(init=False)              # Magic ('koly')
    Version: int = field(init=False)                # Current version is 4
    HeaderSize: int = field(init=False)             # sizeof(this), always 512
    Flags: int = field(init=False)                  # Flags
    RunningDataForkOffset: int = field(init=False)  #
    DataForkOffset: int = field(init=False)         # Data fork offset (usually 0, beginning of file)
    DataForkLength: int = field(init=False)         # Size of data fork (usually up to the XMLOffset, below),
                                                    # memory image in the UDIF file, in bytes.
    RsrcForkOffset: int = field(init=False)         # Resource fork offset, if any
    RsrcForkLength: int = field(init=False)         # Resource fork length, if any

    SegmentNumber: int = field(init=False)          # Usually 1, may be 0
    SegmentCount: int = field(init=False)           # Usually 1, may be 0

    SegmentID: bytearray = field(init=False,
                                 repr=False)        # 128-bit GUID identifier of segment (if SegmentNumber !=0)

    DataChecksumType: int = field(init=False)       # Data fork
    DataChecksumSize: int = field(init=False)       # Checksum Information
    DataChecksum: List[int] = field(init=False,
                                    repr=False)     # Up to 128-bytes (32 x 4) of checksum (uint32_t DataChecksum[32])

    XMLOffset: int = field(init=False)              # Offset of property list in DMG, from beginning
    XMLLength: int = field(init=False)              # Length of property list

    Reserved1: bytes = field(init=False,
                             repr=False)            # 120 reserved bytes - zeroed

    ChecksumType: int = field(init=False)           # Master
    ChecksumSize: int = field(init=False)           # Checksum information
    Checksum: int = field(init=False, repr=False)   # Up to 128-bytes (32 x 4) of checksum

    ImageVariant: int = field(init=False)           # Commonly 1
    SectorCount: int = field(init=False)            # Size of DMG when expanded, in sectors

    reserved2: int = field(init=False, repr=False)  # 0
    reserved3: int = field(init=False, repr=False)  # 0
    reserved4: int = field(init=False, repr=False)  # 0

    def __post_init__(self):
        data = BinaryParser(self.file_path, self.offset)
        self.Signature = data.get_char_arr(4).decode()
        self.Version = data.get_int(signed=False)
        self.HeaderSize = data.get_int(signed=False)
        self.Flags = data.get_int(signed=False)

        self.RunningDataForkOffset = data.get_ll(signed=False)
        self.DataForkOffset = data.get_ll(signed=False)
        self.DataForkLength = data.get_ll(signed=False)
        self.RsrcForkOffset = data.get_ll(signed=False)
        self.RsrcForkLength = data.get_ll(signed=False)

        self.SegmentNumber = data.get_int(signed=False)
        self.SegmentCount = data.get_int(signed=False)

        if self.SegmentNumber != 0:
            self.SegmentID = data.get_char_arr(16)
        else:
            # TODO: what if SegmentNumber is 0?
            #  in doc whe should only parse this if (self.SegmentNumber != 0)
            #  but in realty this field is still there just zeroed out
            self.SegmentID = data.get_char_arr(16)

        self.DataChecksumType = data.get_int(signed=False)
        self.DataChecksumSize = data.get_int(signed=False)
        self.DataChecksum = data.get_char_arr(32 * 4)

        self.XMLOffset = data.get_ll(signed=False)
        self.XMLLength = data.get_ll(signed=False)

        self.Reserved1 = data.get_char_arr(30 * 4)

        self.ChecksumType = data.get_int(signed=False)
        self.ChecksumSize = data.get_int(signed=False)
        self.Checksum = data.get_char_arr(32 * 4)

        self.ImageVariant = data.get_int(signed=False)
        self.SectorCount = data.get_ll(signed=False)

        self.reserved2 = data.get_int(signed=False)
        self.reserved3 = data.get_int(signed=False)
        self.reserved4 = data.get_int(signed=False)


@dataclass()
class RawBlock:
    """ base class for object parsed from byte array """
    raw_block_data: str = field(repr=False)


@dataclass
class UDIFChecksum(RawBlock):
    """ UDIFChecksum, Not sure how this is calculated"""
    Type: int = field(init=False)
    ChecksumSize: int = field(init=False)
    Data: bytes = field(init=False, repr=False)

    def __post_init__(self):
        data = BinaryParser(self.raw_block_data)
        self.Type = data.get_int(signed=False)
        self.ChecksumSize = data.get_int(signed=False)
        self.Data = data.get_char_arr(128)


@dataclass
class BLKXChunk(RawBlock):
    """ A specific chunk of data, part of a volume"""

    # BLKXTable fields:
    # =============

    EntryType: str = field(init=False)
    # Compression type used or entry type:
    # 0x00000000	---	Zero-Fill
    # 0x00000001	UDRW/UDRO	RAW or NULL compression (uncompressed)
    # 0x00000002	---	Ignored/unknown
    # 0x80000004	UDCO	Apple Data Compression (ADC)
    # 0x80000005	UDZO	zLib data compression
    # 0x80000006	UDBZ	bz2lib data compression
    # 0x7ffffffe	---	No blocks - Comment: +beg and +end
    # 0xffffffff	---	No blocks - Identifies last blxx entry

    entry_type_info: str = field(init=False)
    Comment: int = field(init=False)            # "+beg" or "+end", if EntryType is comment (0x7FFFFFFE). Else reserved.
    SectorNumber: int = field(init=False)       # Start sector of this chunk
    SectorCount: int = field(init=False)        # Number of sectors in this chunk
    CompressedOffset: int = field(init=False)   # Start of chunk in data fork
    CompressedLength: int = field(init=False)   # Count of bytes of chunk, in data fork

    def __post_init__(self):
        data = BinaryParser(self.raw_block_data)
        self.EntryType = hex(data.get_int(signed=False))
        self.entry_type_info = entry_type_translation[self.EntryType]
        self.Comment = data.get_int(signed=False)
        self.SectorNumber = data.get_ll(signed=False)
        self.SectorCount = data.get_ll(signed=False)
        self.CompressedOffset = data.get_ll(signed=False)
        self.CompressedLength = data.get_ll(signed=False)


@dataclass
class BLKXTable:
    """ Holds metadata on one volume in the dmg. where are it's chucks located in the bin DMG file, what compression
    and so on.."""
    ID: str
    Name: str

    Attributes: str
    Data: bytes = field(repr=False)
    CFName: Optional[str] = field(default=None)

    # BLKXTable fields:
    # =============
    Signature: str = field(init=False)          # Magic ('mish')
    Version: int = field(init=False)            # Current version is 1
    SectorNumber: int = field(init=False)       # Starting disk sector in this blkx descriptor
    SectorCount: int = field(init=False)        # Number of disk sectors in this blkx descriptor

    DataOffset: int = field(init=False)
    BuffersNeeded: int = field(init=False)
    BlockDescriptors: int = field(init=False)   # Number of descriptors

    reserved1: int = field(init=False, repr=False)
    reserved2: int = field(init=False, repr=False)
    reserved3: int = field(init=False, repr=False)
    reserved4: int = field(init=False, repr=False)
    reserved5: int = field(init=False, repr=False)
    reserved6: int = field(init=False, repr=False)

    checksum: UDIFChecksum = field(init=False)

    NumberOfBlockChunks: int = field(init=False)
    BLKXChunkEntry: List[BLKXChunk] = field(default_factory=list)

    def __post_init__(self):
        data = BinaryParser(self.Data)
        self.Signature = data.get_char_arr(4).decode()
        self.Version = data.get_int(signed=False)
        self.SectorNumber = data.get_ll(signed=False)
        self.SectorCount = data.get_ll(signed=False)

        self.DataOffset = data.get_ll(signed=False)
        self.BuffersNeeded = data.get_int(signed=False)
        self.BlockDescriptors = data.get_int(signed=False)

        self.reserved1 = data.get_int(signed=False)
        self.reserved2 = data.get_int(signed=False)
        self.reserved3 = data.get_int(signed=False)
        self.reserved4 = data.get_int(signed=False)
        self.reserved5 = data.get_int(signed=False)
        self.reserved6 = data.get_int(signed=False)

        self.checksum = UDIFChecksum(data.get_char_arr(136))

        self.NumberOfBlockChunks = data.get_int(signed=False)
        for _ in range(self.NumberOfBlockChunks):
            self.BLKXChunkEntry.append(BLKXChunk(data.get_byte_arr(40)))
        # print(self.BLKXChunkEntry)


@dataclass
class ContentPlist(Block):
    """ Plist that usually contains the different volumes, and their chucks location and compression in order to re
    assumable them. """
    length: int
    raw: bytes = field(init=False, repr=False)
    content: dict = field(init=False, repr=False)
    blkx: List[BLKXTable] = field(default_factory=list)

    def __post_init__(self):
        fp = open(self.file_path, "rb")
        fp.seek(self.offset)
        self.raw = fp.read(self.length - 1)
        self.content = plistlib.loads(self.raw)
        for blkx_table in self.content.get("resource-fork", {}).get("blkx", []):
            self.blkx.append(BLKXTable(**blkx_table))
            # print(self.blkx[_name])
        for plst in self.content.get("resource-fork", {}).get("blkx", []):
            # TODO: what to do with this?
            pass

@dataclass
class DMG:
    """ Parse DMG metadata from dmg file """
    file_path: str
    file_size: int = field(init=False, repr=False)
    file_name: str = field(init=False, repr=False)
    sha256: str = field(init=False)
    md5: str = field(init=False, repr=False)
    # DMG fields:
    # =============
    koly_block: KolyBlock = field(init=False)
    content_plist: Optional[ContentPlist] = field(init=False)

    def __post_init__(self):
        if not os.path.isfile(self.file_path):
            DMGUtilsError(f"Not a file '{self.file_name}'")
        elif not is_dmg(self.file_path):
            DMGUtilsError(f"Not a DMG file '{self.file_name}'")

        self.file_name = os.path.basename(self.file_path)
        self.sha256, self.md5 = calc_hashes(self.file_path)

        stat = os.stat(self.file_path)
        self.file_size = stat.st_size
        koly_offset = self.file_size - 512
        self.koly_block = KolyBlock(self.file_path, offset=koly_offset)
        try:
            self.content_plist = ContentPlist(self.file_path, offset=self.koly_block.XMLOffset,
                                              length=self.koly_block.XMLLength)
        except Exception:
            logger.exception(f"['{self.file_name}'] Failed to parse plist containing the blkx tables")
            self.content_plist = None
        self.dmg_fp = open(self.file_path, "rb")

    def as_dict(self, _filter=False) -> dict:
        """
        :param _filter: removes some of the tmp used during the obj build process
        :returns dmg metadata as dict
        """
        if _filter:
            return asdict(self, dict_factory=self.__filter)
        else:
            return asdict(self)

    def as_json_str(self, indent=2, _filter=False):
        """
        convert dmg metadata to json
        :param indent: indent for json.dumps()
        :param _filter: removes some of the tmp used during the obj build process
        :return: json string
        """
        return json.dumps(self.as_dict(_filter=_filter), indent=indent, default=self._json_serialize)

    def __filter(self, obj):
        """ filter some internal/long/irrelevant fields """
        filtered_keys = ['file_path', "Data", "raw_block_data", "Reserved1", "raw"]
        if isinstance(obj, list):
            return dict([t for t in obj if t[0] not in filtered_keys])
        elif isinstance(obj, dict):
            return {k: self.__filter(v) for k, v in obj.items()
                    if k not in filtered_keys}
        else:
            return dict(obj)
    @staticmethod
    def _json_serialize(obj: Any) -> str:
        """ best effort at serializing bytes data """
        if isinstance(obj, bytes):
            if len(obj) < 256:
                try:
                    return obj.hex()
                except Exception:
                    pass
            else:
                try:
                    return obj.decode()
                except Exception:
                    pass
        return '<not serializable>'

    # Decompress DMG
    # ===============
    def _decompress_blkx(self, blkx: BLKXTable, write_path: str):
        """
        Decompress blkx table representing a volume in the dmg
        :param write_path: destination folder
        """
        file_name = f"{blkx.ID}: {_slugify(blkx.Name)}"
        file_path = os.path.join(write_path, file_name)

        with open(file_path, "wb") as target_fp:
            for blkx_chunk in blkx.BLKXChunkEntry:
                if blkx_chunk.EntryType == "0x80000005":  # zlib
                    self.dmg_fp.seek(blkx_chunk.CompressedOffset)
                    target_fp.write(self.dmg_fp.read(blkx_chunk.CompressedLength))
                # TODO: support more methods

    def decompress_dmg(self, write_path: str):
        """
        Decompress a dmg, meaning unpack and build dmg volumes according to plist
        :param write_path: destination folder
        """
        os.makedirs(write_path, exist_ok=True)
        section = self.content_plist.blkx
        for section in section:
            self._decompress_blkx(section, write_path)
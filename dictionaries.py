#!/usr/bin/env python3
# Created by Ziv Kaspersky <ziv.k@airoav.com> at 2019-07-17
#     ____    _      ____     ____ _    __
#    /    |  (_)____/ __ \   /    | |  / /
#   / /_| | / / ___/ / / /  / /_| | | / /
#  / ___  |/ / /  / /_/ /  / ___  | |/ /
# /_/   |_/_/_/   \____/  /_/   |_|___/

# Standard packages
import logging


logger = logging.getLogger(__name__)

# TODO: add num -> type name, and validate what are the values here
# class ChecksumType(Enum):
#     Sha1 = 1
#     Sha256 = 2


entry_type_translation = {
    "0x0": "Zero-Fill",
    "0x1": "UDRW/UDRO RAW or NULL compression (uncompressed)",
    "0x2": "Ignored/unknown",
    "0x80000004": "UDCO Apple Data Compression (ADC)",
    "0x80000005": "UDZO zlib data compression",
    "0x80000006": "UDBZ bz2lib data compression",
    "0x80000007": "ULFO LZFSE data compression",
    "0x7ffffffe": "No blocks - Comment: +beg and +end",
    "0xffffffff": "No blocks - Identifies last blkx entry"
}

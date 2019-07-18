# DMG_utils
Some tools to parse and work with Apple DMG format files

## Use example

As simple as:
```python
from DMG_utils import DMG
dmg = DMG(file_path)
```

## Result example

Print the object:
```python
print(dmg)
```

```
DMG(file_path='/tmp/wl/0a735de4c491b8b88db4e74207901986887d6b3c6626b43eb67d5afe77732f55', sha256='0a735de4c491b8b88db4e74207901986887d6b3c6626b43eb67d5afe77732f55', koly_block=KolyBlock(offset=125317, Signature='koly', Version=4, HeaderSize=512, Flags=1, RunningDataForkOffset=0, DataForkOffset=0, DataForkLength=116991, RsrcForkOffset=0, RsrcForkLength=0, SegmentNumber=1, SegmentCount=1, DataChecksumType=2, DataChecksumSize=32, XMLOffset=116991, XMLLength=8326, ChecksumType=2, ChecksumSize=32, ImageVariant=1, SectorCount=68608), content_plist=ContentPlist(offset=116991, length=8326, blkx=[BLKXTable(ID='-1', Name='Protective Master Boot Record (MBR : 0)', Attributes='0x0050', CFName='Protective Master Boot Record (MBR : 0)', Signature='mish', Version=1, SectorNumber=0, SectorCount=1, DataOffset=0, BuffersNeeded=2049, BlockDescriptors=0, checksum=UDIFChecksum(Type=2, ChecksumSize=32), NumberOfBlockChunks=2, BLKXChunkEntry=[BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=0, SectorCount=1, CompressedOffset=0, CompressedLength=54), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0)]), BLKXTable(ID='0', Name='GPT Header (Primary GPT Header : 1)', Attributes='0x0050', CFName='GPT Header (Primary GPT Header : 1)', Signature='mish', Version=1, SectorNumber=1, SectorCount=1, DataOffset=0, BuffersNeeded=2049, BlockDescriptors=1, checksum=UDIFChecksum(Type=2, ChecksumSize=32), NumberOfBlockChunks=2, BLKXChunkEntry=[BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=0, SectorCount=1, CompressedOffset=54, CompressedLength=106), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0)]), BLKXTable(ID='1', Name='GPT Partition Data (Primary GPT Table : 2)', Attributes='0x0050', CFName='GPT Partition Data (Primary GPT Table : 2)', Signature='mish', Version=1, SectorNumber=2, SectorCount=32, DataOffset=0, BuffersNeeded=2049, BlockDescriptors=2, checksum=UDIFChecksum(Type=2, ChecksumSize=32), NumberOfBlockChunks=2, BLKXChunkEntry=[BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=0, SectorCount=32, CompressedOffset=160, CompressedLength=227), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0)]), BLKXTable(ID='2', Name=' (Apple_Free : 3)', Attributes='0x0050', CFName=' (Apple_Free : 3)', Signature='mish', Version=1, SectorNumber=34, SectorCount=6, DataOffset=0, BuffersNeeded=0, BlockDescriptors=3, checksum=UDIFChecksum(Type=2, ChecksumSize=32), NumberOfBlockChunks=2, BLKXChunkEntry=[BLKXChunk(EntryType='0x2', entry_type_info='Ignored/unknown', Comment=0, SectorNumber=0, SectorCount=6, CompressedOffset=387, CompressedLength=0), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0)]), BLKXTable(ID='3', Name='disk image (Apple_HFS : 4)', Attributes='0x0050', CFName='disk image (Apple_HFS : 4)', Signature='mish', Version=1, SectorNumber=40, SectorCount=68528, DataOffset=0, BuffersNeeded=2271, BlockDescriptors=4, checksum=UDIFChecksum(Type=2, ChecksumSize=32), NumberOfBlockChunks=9, BLKXChunkEntry=[BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=0, SectorCount=1072, CompressedOffset=387, CompressedLength=1027), BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=6352, SectorCount=528, CompressedOffset=1414, CompressedLength=1395), BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=12160, SectorCount=336, CompressedOffset=2809, CompressedLength=113707), BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=68526, SectorCount=1, CompressedOffset=116516, CompressedLength=141), BLKXChunk(EntryType='0xffffffff', entry_type_info='No blocks - Identifies last blkx entry', Comment=0, SectorNumber=68528, SectorCount=0, CompressedOffset=116657, CompressedLength=0), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0)]), BLKXTable(ID='4', Name=' (Apple_Free : 5)', Attributes='0x0050', CFName=' (Apple_Free : 5)', Signature='mish', Version=1, SectorNumber=68568, SectorCount=7, DataOffset=0, BuffersNeeded=0, BlockDescriptors=5, checksum=UDIFChecksum(Type=2, ChecksumSize=32), NumberOfBlockChunks=2, BLKXChunkEntry=[BLKXChunk(EntryType='0x2', entry_type_info='Ignored/unknown', Comment=0, SectorNumber=0, SectorCount=7, CompressedOffset=116657, CompressedLength=0), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0)]), BLKXTable(ID='5', Name='GPT Partition Data (Backup GPT Table : 6)', Attributes='0x0050', CFName='GPT Partition Data (Backup GPT Table : 6)', Signature='mish', Version=1, SectorNumber=68575, SectorCount=32, DataOffset=0, BuffersNeeded=2049, BlockDescriptors=6, checksum=UDIFChecksum(Type=2, ChecksumSize=32), NumberOfBlockChunks=2, BLKXChunkEntry=[BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=0, SectorCount=32, CompressedOffset=116657, CompressedLength=227), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0)]), BLKXTable(ID='6', Name='GPT Header (Backup GPT Header : 7)', Attributes='0x0050', CFName='GPT Header (Backup GPT Header : 7)', Signature='mish', Version=1, SectorNumber=68607, SectorCount=1, DataOffset=0, BuffersNeeded=2049, BlockDescriptors=7, checksum=UDIFChecksum(Type=2, ChecksumSize=32), NumberOfBlockChunks=2, BLKXChunkEntry=[BLKXChunk(EntryType='0x80000007', entry_type_info='ULFO LZFSE data compression', Comment=0, SectorNumber=0, SectorCount=1, CompressedOffset=116884, CompressedLength=107), BLKXChunk(EntryType='0x0', entry_type_info='Zero-Fill', Comment=0, SectorNumber=0, SectorCount=0, CompressedOffset=0, CompressedLength=0)])]))
```

As json:
```python
print(dmg.as_json_str(_filter=True))
```

```json
{
  "file_size": 125829,
  "file_name": "0a735de4c491b8b88db4e74207901986887d6b3c6626b43eb67d5afe77732f55",
  "sha256": "0a735de4c491b8b88db4e74207901986887d6b3c6626b43eb67d5afe77732f55",
  "md5": "341600bd63cd4d23c7ed0c026eb024d2",
  "koly_block": {
    "offset": 125317,
    "Signature": "koly",
    "Version": 4,
    "HeaderSize": 512,
    "Flags": 1,
    "RunningDataForkOffset": 0,
    "DataForkOffset": 0,
    "DataForkLength": 116991,
    "RsrcForkOffset": 0,
    "RsrcForkLength": 0,
    "SegmentNumber": 1,
    "SegmentCount": 1,
    "SegmentID": "af3f4d59ee2543fabbe59d7eb3dcd14a",
    "DataChecksumType": 2,
    "DataChecksumSize": 32,
    "DataChecksum": "77d9942200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "XMLOffset": 116991,
    "XMLLength": 8326,
    "ChecksumType": 2,
    "ChecksumSize": 32,
    "Checksum": "8f06d3ef00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "ImageVariant": 1,
    "SectorCount": 68608,
    "reserved2": 0,
    "reserved3": 0,
    "reserved4": 0
  },
  "content_plist": {
    "offset": 116991,
    "length": 8326,
    "content": {
      "resource-fork": {
        "blkx": [
          {
            "Attributes": "0x0050",
            "CFName": "Protective Master Boot Record (MBR : 0)",
            "Data": "<not serializable>",
            "ID": "-1",
            "Name": "Protective Master Boot Record (MBR : 0)"
          },
          {
            "Attributes": "0x0050",
            "CFName": "GPT Header (Primary GPT Header : 1)",
            "Data": "<not serializable>",
            "ID": "0",
            "Name": "GPT Header (Primary GPT Header : 1)"
          },
          {
            "Attributes": "0x0050",
            "CFName": "GPT Partition Data (Primary GPT Table : 2)",
            "Data": "<not serializable>",
            "ID": "1",
            "Name": "GPT Partition Data (Primary GPT Table : 2)"
          },
          {
            "Attributes": "0x0050",
            "CFName": " (Apple_Free : 3)",
            "Data": "<not serializable>",
            "ID": "2",
            "Name": " (Apple_Free : 3)"
          },
          {
            "Attributes": "0x0050",
            "CFName": "disk image (Apple_HFS : 4)",
            "Data": "<not serializable>",
            "ID": "3",
            "Name": "disk image (Apple_HFS : 4)"
          },
          {
            "Attributes": "0x0050",
            "CFName": " (Apple_Free : 5)",
            "Data": "<not serializable>",
            "ID": "4",
            "Name": " (Apple_Free : 5)"
          },
          {
            "Attributes": "0x0050",
            "CFName": "GPT Partition Data (Backup GPT Table : 6)",
            "Data": "<not serializable>",
            "ID": "5",
            "Name": "GPT Partition Data (Backup GPT Table : 6)"
          },
          {
            "Attributes": "0x0050",
            "CFName": "GPT Header (Backup GPT Header : 7)",
            "Data": "<not serializable>",
            "ID": "6",
            "Name": "GPT Header (Backup GPT Header : 7)"
          }
        ],
        "plst": [
          {
            "Attributes": "0x0050",
            "Data": "\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0001\u0000\u0001\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000",
            "ID": "0",
            "Name": ""
          }
        ]
      }
    },
    "blkx": [
      {
        "ID": "-1",
        "Name": "Protective Master Boot Record (MBR : 0)",
        "Attributes": "0x0050",
        "CFName": "Protective Master Boot Record (MBR : 0)",
        "Signature": "mish",
        "Version": 1,
        "SectorNumber": 0,
        "SectorCount": 1,
        "DataOffset": 0,
        "BuffersNeeded": 2049,
        "BlockDescriptors": 0,
        "reserved1": 0,
        "reserved2": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "reserved6": 0,
        "checksum": {
          "Type": 2,
          "ChecksumSize": 32
        },
        "NumberOfBlockChunks": 2,
        "BLKXChunkEntry": [
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 1,
            "CompressedOffset": 0,
            "CompressedLength": 54
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          }
        ]
      },
      {
        "ID": "0",
        "Name": "GPT Header (Primary GPT Header : 1)",
        "Attributes": "0x0050",
        "CFName": "GPT Header (Primary GPT Header : 1)",
        "Signature": "mish",
        "Version": 1,
        "SectorNumber": 1,
        "SectorCount": 1,
        "DataOffset": 0,
        "BuffersNeeded": 2049,
        "BlockDescriptors": 1,
        "reserved1": 0,
        "reserved2": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "reserved6": 0,
        "checksum": {
          "Type": 2,
          "ChecksumSize": 32
        },
        "NumberOfBlockChunks": 2,
        "BLKXChunkEntry": [
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 1,
            "CompressedOffset": 54,
            "CompressedLength": 106
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          }
        ]
      },
      {
        "ID": "1",
        "Name": "GPT Partition Data (Primary GPT Table : 2)",
        "Attributes": "0x0050",
        "CFName": "GPT Partition Data (Primary GPT Table : 2)",
        "Signature": "mish",
        "Version": 1,
        "SectorNumber": 2,
        "SectorCount": 32,
        "DataOffset": 0,
        "BuffersNeeded": 2049,
        "BlockDescriptors": 2,
        "reserved1": 0,
        "reserved2": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "reserved6": 0,
        "checksum": {
          "Type": 2,
          "ChecksumSize": 32
        },
        "NumberOfBlockChunks": 2,
        "BLKXChunkEntry": [
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 32,
            "CompressedOffset": 160,
            "CompressedLength": 227
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          }
        ]
      },
      {
        "ID": "2",
        "Name": " (Apple_Free : 3)",
        "Attributes": "0x0050",
        "CFName": " (Apple_Free : 3)",
        "Signature": "mish",
        "Version": 1,
        "SectorNumber": 34,
        "SectorCount": 6,
        "DataOffset": 0,
        "BuffersNeeded": 0,
        "BlockDescriptors": 3,
        "reserved1": 0,
        "reserved2": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "reserved6": 0,
        "checksum": {
          "Type": 2,
          "ChecksumSize": 32
        },
        "NumberOfBlockChunks": 2,
        "BLKXChunkEntry": [
          {
            "EntryType": "0x2",
            "entry_type_info": "Ignored/unknown",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 6,
            "CompressedOffset": 387,
            "CompressedLength": 0
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          }
        ]
      },
      {
        "ID": "3",
        "Name": "disk image (Apple_HFS : 4)",
        "Attributes": "0x0050",
        "CFName": "disk image (Apple_HFS : 4)",
        "Signature": "mish",
        "Version": 1,
        "SectorNumber": 40,
        "SectorCount": 68528,
        "DataOffset": 0,
        "BuffersNeeded": 2271,
        "BlockDescriptors": 4,
        "reserved1": 0,
        "reserved2": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "reserved6": 0,
        "checksum": {
          "Type": 2,
          "ChecksumSize": 32
        },
        "NumberOfBlockChunks": 9,
        "BLKXChunkEntry": [
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 1072,
            "CompressedOffset": 387,
            "CompressedLength": 1027
          },
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 6352,
            "SectorCount": 528,
            "CompressedOffset": 1414,
            "CompressedLength": 1395
          },
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 12160,
            "SectorCount": 336,
            "CompressedOffset": 2809,
            "CompressedLength": 113707
          },
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 68526,
            "SectorCount": 1,
            "CompressedOffset": 116516,
            "CompressedLength": 141
          },
          {
            "EntryType": "0xffffffff",
            "entry_type_info": "No blocks - Identifies last blkx entry",
            "Comment": 0,
            "SectorNumber": 68528,
            "SectorCount": 0,
            "CompressedOffset": 116657,
            "CompressedLength": 0
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          }
        ]
      },
      {
        "ID": "4",
        "Name": " (Apple_Free : 5)",
        "Attributes": "0x0050",
        "CFName": " (Apple_Free : 5)",
        "Signature": "mish",
        "Version": 1,
        "SectorNumber": 68568,
        "SectorCount": 7,
        "DataOffset": 0,
        "BuffersNeeded": 0,
        "BlockDescriptors": 5,
        "reserved1": 0,
        "reserved2": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "reserved6": 0,
        "checksum": {
          "Type": 2,
          "ChecksumSize": 32
        },
        "NumberOfBlockChunks": 2,
        "BLKXChunkEntry": [
          {
            "EntryType": "0x2",
            "entry_type_info": "Ignored/unknown",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 7,
            "CompressedOffset": 116657,
            "CompressedLength": 0
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          }
        ]
      },
      {
        "ID": "5",
        "Name": "GPT Partition Data (Backup GPT Table : 6)",
        "Attributes": "0x0050",
        "CFName": "GPT Partition Data (Backup GPT Table : 6)",
        "Signature": "mish",
        "Version": 1,
        "SectorNumber": 68575,
        "SectorCount": 32,
        "DataOffset": 0,
        "BuffersNeeded": 2049,
        "BlockDescriptors": 6,
        "reserved1": 0,
        "reserved2": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "reserved6": 0,
        "checksum": {
          "Type": 2,
          "ChecksumSize": 32
        },
        "NumberOfBlockChunks": 2,
        "BLKXChunkEntry": [
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 32,
            "CompressedOffset": 116657,
            "CompressedLength": 227
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          }
        ]
      },
      {
        "ID": "6",
        "Name": "GPT Header (Backup GPT Header : 7)",
        "Attributes": "0x0050",
        "CFName": "GPT Header (Backup GPT Header : 7)",
        "Signature": "mish",
        "Version": 1,
        "SectorNumber": 68607,
        "SectorCount": 1,
        "DataOffset": 0,
        "BuffersNeeded": 2049,
        "BlockDescriptors": 7,
        "reserved1": 0,
        "reserved2": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "reserved6": 0,
        "checksum": {
          "Type": 2,
          "ChecksumSize": 32
        },
        "NumberOfBlockChunks": 2,
        "BLKXChunkEntry": [
          {
            "EntryType": "0x80000007",
            "entry_type_info": "ULFO LZFSE data compression",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 1,
            "CompressedOffset": 116884,
            "CompressedLength": 107
          },
          {
            "EntryType": "0x0",
            "entry_type_info": "Zero-Fill",
            "Comment": 0,
            "SectorNumber": 0,
            "SectorCount": 0,
            "CompressedOffset": 0,
            "CompressedLength": 0
          }
        ]
      }
    ]
  }
}
```

## Requirements

* python <3.7
* `pip install -r requirements.txt`
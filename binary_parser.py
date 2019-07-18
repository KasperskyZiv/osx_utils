#!/usr/bin/env python3
# Created by Ziv Kaspersky <ziv.k@airoav.com> at 2019-07-16
#     ____    _      ____     ____ _    __
#    /    |  (_)____/ __ \   /    | |  / /
#   / /_| | / / ___/ / / /  / /_| | | / /
#  / ___  |/ / /  / /_/ /  / ___  | |/ /
# /_/   |_/_/_/   \____/  /_/   |_|___/

# Standard packages
import logging
from io import BytesIO
from typing import Union, IO, Any

logger = logging.getLogger(__name__)


class BinaryParser:
    """Main object containing all the necessary functions to parse
    binary data.
    """
    _file: IO[Any]

    def __init__(self, fp: Union[str, bytes], offset=None):
        if isinstance(fp, str):
            self._file = open(fp, "rb")
        elif isinstance(fp, bytes):
            self._file = BytesIO(fp)
        else:
            raise Exception(f"unexpected arg type {type(fp)}")
        if offset:
            self._file.seek(offset)
        self.__is_little_endian = False  # i think it's big

    def get_raw_string(self) -> bytearray:
        """Read a null-terminated string from file."""

        string = bytearray()

        c = self._file.read(1)

        while c not in (b'\x00', ''):
            string += c
            c = self._file.read(1)
        return string

    def get_string(self) -> str:
        """Read a Utf-8 null-terminated string from file."""
        return self.get_raw_string().decode('utf-8', errors='replace')

    def get_int(self, signed=False):
        """Read a 4-byte integer from file, account for endian-ness."""

        integer = self._file.read(4)

        if self.__is_little_endian:
            return int.from_bytes(integer, byteorder='little', signed=signed)

        return int.from_bytes(integer, byteorder='big', signed=signed)

    def get_ll(self, signed=False):
        """Read an 8-byte long long from file, account for endian-ness."""

        longlong = self._file.read(8)

        if self.__is_little_endian:
            return int.from_bytes(longlong, byteorder='little', signed=signed)

        return int.from_bytes(longlong, byteorder='big', signed=signed)

    def get_char_arr(self, length):
        """ Read a char[length] from file. """
        return self._file.read(length)

    def get_byte_arr(self, length):
        """ Read a byte[length] from file. """
        return self._file.read(length * 2)

    def get_int_arr(self, length, signed=False):
        """ Read an int[length] from file. """
        return [self.get_int(signed=signed) for _ in range(length)]

    def get_ll_arr(self, length, signed=False):
        """ Read an ll[length] from file. """
        return [self.get_ll(signed=signed) for _ in range(length)]

    def get_until_end(self):
        """ Read until EOF """
        return self._file.read()

#!/usr/bin/env python3
# Created by Ziv Kaspersky <ziv.k@airoav.com> at 2019-07-17
#     ____    _      ____     ____ _    __
#    /    |  (_)____/ __ \   /    | |  / /
#   / /_| | / / ___/ / / /  / /_| | | / /
#  / ___  |/ / /  / /_/ /  / ___  | |/ /
# /_/   |_/_/_/   \____/  /_/   |_|___/

# Standard packages
import hashlib
import logging
import os
from typing import Tuple

# External packages
import magic

logger = logging.getLogger(__name__)


def _slugify(value: str) -> str:
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    # import unicodedata
    # value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    # value = re.sub('[^\w\s-]', '', value).strip().lower()
    # value = re.sub('[-\s]+', '-', value)
    return value


def is_dmg(file_path: str) -> bool:
    with open(file_path, 'rb') as f:
        f.seek(0, 2)
        file_size = f.tell()
        if file_size < 512:
            return False
        f.seek(-512, os.SEEK_END)
        s = f.read(4)
        if s != b'koly':
            return False
        else:
            # TODO: is this correct? arn't we missing something? what if type not in this list. but what if the file
            #  is not dmg but happens to have "koly" value in the place?
            # TODO: dose this include Vox?
            return magic.from_file(file_path, mime=True) in ["application/zlib",
                                                             "application/octet-stream",
                                                             "application/x-apple-diskimage",
                                                             "application/x-bzip2"]



def calc_hashes(file_path: str) -> Tuple[str, str]:
    """
    Calculate sha256 and md5
    :param file_path: path to file
    :return: (sha256, md5)
    """
    sha256 = hashlib.sha256()
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            sha256.update(data)
            md5.update(data)
    return sha256.hexdigest(), md5.hexdigest()

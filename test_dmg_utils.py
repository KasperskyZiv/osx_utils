#!/usr/bin/env python3
# Created by Ziv Kaspersky <ziv.k@airoav.com> at 2019-07-17
#     ____    _      ____     ____ _    __
#    /    |  (_)____/ __ \   /    | |  / /
#   / /_| | / / ___/ / / /  / /_| | | / /
#  / ___  |/ / /  / /_/ /  / ___  | |/ /
# /_/   |_/_/_/   \____/  /_/   |_|___/

# Standard packages
import json
import logging
import os

# Proprietary packages
from dmg import DMG
from utils import is_dmg

logger = logging.getLogger("DMG_Util_Test")

_format = "[%(name)s](%(levelname)s): %(message)s"
logging.basicConfig(format=_format, level=logging.DEBUG)

# FILE_PATH = "/tmp/1/3a71ce0f602096b25eb50187df069ed3a683de8d2e95535fd2f2f9c70129e80f"
FILE_PATH = "/tmp/wl/0a735de4c491b8b88db4e74207901986887d6b3c6626b43eb67d5afe77732f55"
# b4135907cb54514add2fd95993918d9d51cc0f937984fb09dc4972fa89fca3e4
# f815c5dba409ff728a89eb611ae22c8dd892d127fc5a54c10fad287424952d4a
# folder_path = "/Users/zivkaspersky/work/malwares/dmg"
folder_path = "/tmp/wl"
save_path = os.path.join(folder_path, "reports")


def test_get_all():
    os.makedirs(save_path, exist_ok=True)
    for f_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, f_name)
        if os.path.isfile(file_path):
            try:
                logger.info(f"File '{file_path}' {'Is DMG' if is_dmg(file_path) else 'Not a DMG'}")
                dmg = DMG(file_path)
                with open(os.path.join(save_path, f"{f_name}.json"), "w") as fp:
                    json.dump(dmg.as_dict(), fp, indent=2, default=DMG._json_serialize)
            except Exception:
                pass


def test_run_on_one_file():
    file_path = FILE_PATH
    logger.info(f"File '{file_path}' {'Is DMG' if is_dmg(file_path) else 'Not a DMG'}")
    dmg = DMG(file_path)
    print(dmg)

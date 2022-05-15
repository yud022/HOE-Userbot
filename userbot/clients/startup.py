# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

import telethon.utils

from userbot import BOT_VER as version
from userbot import (
    DEFAULT,
    DEVS,
    LOGS,
    HOE2,
    HOE3,
    HOE4,
    HOE5,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_SESSION,
    blacklistayiin,
    bot,
    call_py,
)
from userbot.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nHOE-UserBot v{}, Copyright © 2021-2022 YUD• <https://github.com/yud022>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH KONTOL, USERBOT {} GUA BASMI NAJIS BANGET DIPAKE JAMET KEK LU.\nHOE-UserBot v{}, Copyright © 2021-2022 ʀɪsᴍᴀɴ• <https://github.com/yud022>"


async def ayiin_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


def multiayiin():
    if 1700405732 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001675396283 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1700405732 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            bot.loop.run_until_complete(hoe_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e), exc_info=True)

    if STRING_2:
        try:
            HOE2.start()
            HOE2.loop.run_until_complete(hoe_client(HOE2))
            user = HOE2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e), exc_info=True)

    if STRING_3:
        try:
            HOE3.start()
            HOE3.loop.run_until_complete(hoe_client(HOE3))
            user = HOE3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e), exc_info=True)

    if STRING_4:
        try:
            HOE4.start()
            HOE4.loop.run_until_complete(hoe_client(HOE4))
            user = HOE4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e), exc_info=True)

    if STRING_5:
        try:
            AYIIN5.start()
            AYIIN5.loop.run_until_complete(hoe_client(HOE5))
            user = HOE5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e), exc_info=True)

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    return failed

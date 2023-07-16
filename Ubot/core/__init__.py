from pyrogram import filters, Client

from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *

async def ajg(client):
    try:
        await client.join_chat("SiArabSupport")
        await client.join_chat("SiArab_Store")
        await client.join_chat("cehasiarab")
    except BaseException:
        pass

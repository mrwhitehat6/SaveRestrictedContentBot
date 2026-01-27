#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config(30169419
, default=None, cast=int)
API_HASH = config("c8e9a9e23d8c3079b7173b7ff4924460
", default=None)
BOT_TOKEN = config("8389509300:AAFups9-XpAXPDMhsOxx_GVtdhHJyJylonM", default=None)
SESSION = config("1BVtsOI8Bu8OFSz0Eoc6WGloOxPSJD--JUJrAEnD0DgwbiK-hOir2u8wzw2u6R9tfgTyoUeN8uJB9ErS1ALTkcS_27lOnlmhoIKlmehKd_gRb9ky0m1vJRRoyxID2ljSUfJObSls6ic3Mo_jNW771AEmkfiN4BbSmzDI9RCHnUhu5tuorNxONXBsDuZVq03WF6wq4hC0AE_zjbYEbRkKxfhPeHmICb9rLkbwS3lBPe6-Q4rB0qks8n1RWfxKr2v0OQovjKCLjfeB3mEKe1Ku2hBwwCjzWJbUuUnGpVvCLMSvLed4fzrc5vsb0j2yK7g3fAlNserxXlz1AAfTgz6wJDSY0QtHd8vA=", default=None)
FORCESUB = config("saverestrictedchannel", default=None)
AUTH = config(6283515337, default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

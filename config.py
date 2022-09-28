## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAC_zjdBa0g-nILJ8jfdBxe20vpoHua-Gznv-a-NrHlvFchTZHYOxx4ZZT7ibgX6pNjHBJdzviZjhsckn4cFsUdtLEOkPN5objm0l5sZeih0YOXIw3Zajr3gRjHZKTXG1cBVfyhpHKMORDvHpjnmGj2xKvYAafnFyV9kxldcamyEP4wiNv3z5w7fxbKYqrv0T-tZsdDH9RbyNtu2vJaxXOg8-ZS6oDxaymOv8vadjXXTCXGh3P53hVMQhflxPgaLebI1Q_J4ynBlhGJzlmseKQ0-2ncBZI1XG2WM1RkCXmQyLqPf3pMA59d7lgfRamGnvccSPnC7IW0RAILEr4_hJe9gAAAAATbRvNcA")
BOT_TOKEN = getenv("BOT_TOKEN", "5454166628:AAE4ZFbQJlz_0WSYEz2m9af6Dt_YaH0VcIo")
BOT_NAME = getenv("BOT_NAME", "mm_92_bot")
API_ID = int(getenv("API_ID", "16240771"))
API_HASH = getenv("API_HASH", "e8717d3a9601531928f27590fb41c44d")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "amiraikb")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "mm_92_bot")
OWNER_ID = getenv("OWNER_ID", "-1001793431302")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "xxxcfbt")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/aaddr2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","https://t.me/aaaxx1z")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/970795c1e604a2f838259.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/aaddr2")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")

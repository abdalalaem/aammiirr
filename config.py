## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAzHxbpcwAfFnhNizqcf9ZyCQn28cd_yYAyf5PNPAkDcYrVKJp0pF7u845TF5wDGgymye5zO3gluDpnGDIGpRV4xE6Qiwv58gxpMVcItJ3hWk4Yddcvj8JTkFuhNj_f97CZ9levR_h5pQ2EM20_F49f3tPuWMTewQG0DbwMmuZ-GIwbmyov92lduveaj70SnmQiKu3l1045jq4Zez0jlHRhmmPfjGJWGkJip6dKgzBm0-vwKCImSWw5oa3o-2yyS7a-EMnrQhnhnKRXE6sB76ZknSx9qtzEcnAr029lHm4zHYYsLD7dr5nAOjR-yiIEPKdvuOcjGrya01h0IMKSsXABAAAAATbRvNcA")
BOT_TOKEN = getenv("BOT_TOKEN", "5705986640:AAF91nxE-OjDytrT9PzBBpIvPg_UCbtzfZE")
BOT_NAME = getenv("BOT_NAME", "mio_00_bot")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZzZzZ5")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_ID = getenv("OWNER_ID", "5214682327")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "xxxcfbt")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "aaddr2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", aaaxx1z"")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")

import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "12857763")) #optional
API_HASH = getenv("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1546776438").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID", "1546776438") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "1345594412").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "0").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN2_ID", "0").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN2_ID", "0").split()))


ADMIN1_ID.append(1345594412)
ADMIN2_ID.append(0)
ADMIN3_ID.append(0)
ADMIN4_ID.append(0)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://fadhil01:fadhil123@fadhil01.s6lkqsq.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6370400384:AAFwvY0EFJy3fbsGccEXLJZT_iMJcgrGqKY")
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "4"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "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")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN", "SHA256:azvkVegsZyKoLxKq30eyBdPZ1+iURKf/rurx70H/nZ4") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "arab") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/fadhilabdat04/ProjectArabUbot01")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001803314750"))
CHANNEL = int(getenv("CHANNEL", "-1001681544718"))
SESSION1 = getenv("SESSION1", "BQAP-GEAWKk1o3ejpMQR4vILM57-8FAQvuwwIoCyX4MRoxu98IJApE84qv0vYgM673PiTNPNL9Fqoc1Ce5gMA5IMUaHoGKsnXPRk3rruhJQKxX8uIvydXx0iizZsZ2ZXgRUkgOHpeYGzCtCAExFjv1uOUaMfE5NHd63eh3cYRRbezjQabggPb-5UkXhIhogn3S-0l27FSUbOL140RojfVPIzjkilqhPZbBKE8ntCN_gZNyM1coSAXNoSwhjmcCqUr3UFk4_SiR07_kjHLmMs7m3xvlY46F-5ZybAeJQmCkaPL88ZYL7iQi7VPfdCyPVZTG7nf04zuB_woSC4Ka8iNxUBC1HojAAAAABr5tUGAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")

##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', ''))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ ! _ ').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ''))
ASS_ID = int(getenv("ASS_ID", ''))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
GROUP = getenv("GROUP", None)
CHANNEL = getenv("CHANNEL", None)
CHANNEL = getenv("CHANNEL", None)
MUST_JOIN = getenv("MUST_JOIN", None)
if update_channel.startswith("@"):
    update_channel = update_channel.replace("@", "")

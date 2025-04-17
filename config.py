import configparser
import json
def load_admins():
    try:
        with open("admins.json", "r") as f:
            return json.load(f)
    except:
        return []

ADMIN_IDS = load_admins()
config = configparser.ConfigParser()
config.read('config.ini')

API_ID = int(config["bot"]["api_id"])
API_HASH = config["bot"]["api_hash"]
BOT_TOKEN = config["bot"]["bot_token"]
STORAGE_CHANNEL = int(config["bot"]["storage_channel"])
MOVIE_CHANNEL = config["bot"]["movie_channel"]
STORAGE_CHANNEL_MULTI = config["bot"]["storage_channel_multi"]
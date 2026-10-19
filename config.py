import json

with open("config.json", "r") as f:
    config = json.load(f)

EMAIL = config["email"]
PASSWORD = config["password"]
API = config["api"]
BOT_API = config["bot_api"]
CHAT_ID = config["chat_id"]
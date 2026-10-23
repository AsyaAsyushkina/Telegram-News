import json
import os

with open("config.json", "r") as f:
    config = json.load(f)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
API = os.getenv("GEMINI_API_KEY")
BOT_API = os.getenv("BOT_API")
CHAT_ID = os.getenv("CHAT_ID")
SYS_PROMPT = os.getenv("SYS_PROMPT")
USER_PROMPT = os.getenv("USER_PROMPT")
SENDERS = ""
senders_env = os.getenv("SENDERS", "")
try:
    SENDERS = json.loads(senders_env)
except (json.JSONDecodeError, TypeError):
    SENDERS = [s.strip() for s in senders_env.split(",") if s.strip()]

# EMAIL = config["email"]
# PASSWORD = config["password"]
# API = config["api"]
# BOT_API = config["bot_api"]
# CHAT_ID = config["chat_id"]
# SYS_PROMPT = config["sys_prompt"]
# USER_PROMPT = config["user_prompt"]
# SENDERS = config["senders"]
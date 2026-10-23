import json
import os

if os.getenv("GEMINI_API_KEY"):
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    API = os.getenv("GEMINI_API_KEY")
    BOT_API = os.getenv("BOT_API")
    CHAT_ID = os.getenv("CHAT_ID")
    SYS_PROMPT = os.getenv("SYS_PROMPT")
    USER_PROMPT = os.getenv("USER_PROMPT")

    senders_env = os.getenv("SENDERS", "[]")
    SENDERS = json.loads(senders_env)
    if isinstance(SENDERS, str):
        try:
            SENDERS = json.loads(senders_env)
        except (json.JSONDecodeError, TypeError):
            SENDERS = [
                s.strip() for s in SENDERS.split(',') if s.strip()
            ]

elif os.path.exists("config.json"):
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    EMAIL = config.get("email")
    PASSWORD = config.get("password")
    API = config.get("api")
    BOT_API = config.get("bot_api")
    CHAT_ID = config.get("chat_id")
    SYS_PROMPT = config.get("sys_prompt")
    USER_PROMPT = config.get("user_prompt")
    SENDERS = config.get("senders", [])
else:
    EMAIL = PASSWORD = API = BOT_API = CHAT_ID = SYS_PROMPT = USER_PROMPT = ""
    SENDERS = []
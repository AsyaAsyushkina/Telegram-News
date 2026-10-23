import requests
from config import BOT_API, CHAT_ID

if not BOT_API or not CHAT_ID:
    raise NameError("Bot API key or chat id not set")

url = f"https://api.telegram.org/bot"+BOT_API+"/sendMessage"

def send_message(response_ai):
    payload = {
        "chat_id": CHAT_ID,
        "text": response_ai,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)
    response_data = response.json()

    if response_data.get("ok"):
        print("")
    else:
        print("Failed to send message:", response_data)
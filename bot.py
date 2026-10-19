import requests
import json

with open("config.json", "r") as f:
    config = json.load(f)

url = f"https://api.telegram.org/bot"+config["bot_api"]+"/sendMessage"

payload = {
    "chat_id": config["chat_id"],
    "text": "hello",
    "parse_mode": "Markdown" 
}

response = requests.post(url, json=payload)
response_data = response.json()

if response_data.get("ok"):
    print("Message posted to Telegram successfully!")
else:
    print("Failed to send message:", response_data)
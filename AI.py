from google import genai
import json

with open("config.json", "r") as f:
    config = json.load(f)

client = genai.Client(api_key=config["api"])


response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Hello world!"
)
print(response.text)
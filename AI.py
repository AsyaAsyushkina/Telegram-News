from google import genai
from google.genai import types
from config import API, USER_PROMPT, SYS_PROMPT

if not API or not USER_PROMPT or not SYS_PROMPT:
    raise NameError("API, USER_PROMPT, SYS_PROMPT must be set")

client = genai.Client(api_key=API)

def ai_reprocessing(mail_info):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[USER_PROMPT, mail_info],
        config=types.GenerateContentConfig(
            system_instruction=SYS_PROMPT
        )
    )
    return response.text

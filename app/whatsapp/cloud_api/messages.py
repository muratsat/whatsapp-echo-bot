import requests
from app.config import env 


WHATSAPP_API_URL = "https://graph.facebook.com/v20.0"

FACEBOOK_ACCESS_TOKEN = env.facebook_access_token

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {FACEBOOK_ACCESS_TOKEN}",
}


def send_message(phone_id: str, phone_number: str, message: str):
    if phone_number.startswith("7"):
        phone_number = "78" + phone_number[1:]

    url = f"{WHATSAPP_API_URL}/{phone_id}/messages"

    data = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message
        }
    }

    req = requests.post(url, headers=HEADERS, json=data)

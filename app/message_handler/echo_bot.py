from app.whatsapp.cloud_api.messages import send_message

def handle_message(phone_id: str, phone_number: str, message: str):
    response = f"You said: {message}"
    send_message(phone_id, phone_number, response)

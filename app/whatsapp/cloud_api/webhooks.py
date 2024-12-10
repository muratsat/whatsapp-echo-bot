from typing import Any

from app.message_handler.echo_bot import handle_message
from .schemas import MessageSchema, InteractiveMessageSchema

def handle_webhoook_payload(payload: Any):
    try:
        data = MessageSchema.model_validate(payload)

        for phone_number_id, phone_number, text in _extract_data(data):
            print("Parsed data:", phone_number_id, phone_number, text)
            handle_message(phone_number_id, phone_number, text)

    except Exception as e:
        pass

    try:
        data = InteractiveMessageSchema.model_validate(payload)
        print("Parsed data:", data)
    except Exception as e:
        pass


def _extract_data(data: MessageSchema):
    for entry in data.entry:
        for change in entry.changes:
            if change.field == "messages":
                phone_number_id = change.value.metadata.phone_number_id
                for message in change.value.messages:
                    text = message.text.body
                    phone_number = message.from_
                    yield phone_number_id, phone_number, text


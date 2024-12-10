from typing import List, Optional
from pydantic import BaseModel, Field

class MessageText(BaseModel):
    body: str

class Message(BaseModel):
    from_: str = Field(alias="from")
    id: str
    timestamp: str
    type: str
    text: MessageText

class MessageContact(BaseModel):
    profile: dict
    wa_id: str

class MessageMetadata(BaseModel):
    display_phone_number: str
    phone_number_id: str

class MessageValue(BaseModel):
    messaging_product: str
    metadata: MessageMetadata
    contacts: List[MessageContact]
    messages: Optional[List[Message]]

class MessageChange(BaseModel):
    value: MessageValue
    field: str

class MessageEntry(BaseModel):
    id: str
    changes: List[MessageChange]

class MessageSchema(BaseModel):
    object: str
    entry: List[MessageEntry]

class InteractiveMessageContext(BaseModel):
    from_: str = Field(alias="from")
    id: str


class InteractiveButtonReply(BaseModel):
    id: str
    title: str

class Interactive(BaseModel):
    type: str
    button_reply: InteractiveButtonReply

class InteractiveMessage(BaseModel):
    context: InteractiveMessageContext
    from_: str = Field(alias="from")
    id: str
    timestamp: str
    type: str
    interactive: Interactive


class InteractiveMessageValue(BaseModel):
    messaging_product: str
    metadata: MessageMetadata
    contacts: List[MessageContact]
    messages: Optional[List[InteractiveMessage]]

class InteractiveMessageChange(BaseModel):
    value: InteractiveMessageValue
    field: str

class InteractiveMessageEntry(BaseModel):
    id: str
    changes: List[InteractiveMessageChange]

class InteractiveMessageSchema(BaseModel):
    object: str
    entry: List[InteractiveMessageEntry]

from app.llm.graph import graph
from app.whatsapp.cloud_api.messages import send_message

def handle_message(phone_id: str, phone_number: str, message: str):
    config = { "configurable": { "thread_id": phone_number, "phone_number_id": phone_id } }

    response = graph.invoke({"messages": [("user", message)]}, config)

    send_message(phone_id, phone_number, response["messages"][-1].content)

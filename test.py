from app.llm.graph import graph
from langchain_core.messages import HumanMessage


if __name__ == "__main__":
    thread_id = "42"
    phone_number_id = "483152548211570"

    config = { "configurable": { "thread_id": thread_id, "phone_number_id": phone_number_id } }

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        answer = graph.invoke({"messages": [HumanMessage(content=user_input)]}, config)
        print("Assistant:", answer["messages"][-1].content)


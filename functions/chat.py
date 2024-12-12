from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, AIMessage

llm = ChatOpenAI(model="gpt-4o-mini")

def llm_response(message, history):
    history_langchain_format = []

    for msg in history:
        if msg["role"] == "user":
            history_langchain_format.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            history_langchain_format.append(AIMessage(content=msg["content"]))
    
    history_langchain_format.append(HumanMessage(content=message))
    llm_resposne = llm.invoke(history_langchain_format)

    return llm_resposne.content
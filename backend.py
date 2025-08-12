from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv


load_dotenv()

llm=ChatOpenAI(model='gpt-3.5-turbo-1106')

# print(llm.invoke("Hello, how are you?"))


class chatState(TypedDict):
    messages:Annotated [list[BaseMessage],add_messages]


def chat_node(state:chatState):
    messages= state['messages']
    response=llm.invoke(messages)
    return {"messages": [response]}   

checkpointer=InMemorySaver()
graph= StateGraph(chatState)
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END) 

#bot

chatbot=graph.compile(checkpointer=checkpointer)
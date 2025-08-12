import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage
CONFIG={"configurable":{'thread_id':'thread-1' }}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []



for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])



user_input = st.chat_input("Type your message here...")    

if user_input:
  # adding the user input to the message history
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # invoking the chatbot with the user input
    response = chatbot.invoke({"messages": [HumanMessage(content=user_input)]},config=CONFIG)

    ai_message=response['messages'][-1].content
    #adding the assistant input to the message history
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})

    with st.chat_message("assistant"):
        st.text(ai_message)


   
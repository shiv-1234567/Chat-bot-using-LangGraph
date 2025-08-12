import streamlit as st

# with st.chat_message("user"):
#     st.text("Hello, how are you?")


# with st.chat_message("assistant"):
#     st.text("Hello! I'm doing well, thank you. How can I assist you today?")


# keping the history of chat in the form of a list

# message_history = [] the issue was with this line was that whenevr i press enter in get reset so we need a dict which can retain 
# and for that we have streamlit.session_state a dictionary to keep the history of messages

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


    #adding the assistant input to the message history
    st.session_state['message_history'].append({"role": "assistant", "content": user_input})
    with st.chat_message("assistant"):
        st.text(user_input)



# fundamentals of streanlit is done now lets make real chatbot with gpt model        
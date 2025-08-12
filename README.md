# Chat-bot-using-LangGraph


# 🗨️ LangGraph + Streamlit Chatbot

A stateful AI chatbot built with **[LangGraph](https://python.langchain.com/docs/langgraph)**, **Streamlit**, and **OpenAI GPT models**.  
It provides an interactive web-based chat interface that remembers previous messages in the session, enabling contextual conversations.

---

## 📖 Project Description

This chatbot project demonstrates how to combine **LangGraph's StateGraph** with **Streamlit** to create a fully interactive, stateful AI assistant.  

💬 **What it can do:**
- Carry out multi-turn conversations with context retention.
- Respond intelligently using **OpenAI's GPT models**.
- Render chat history on the UI for a smooth, ChatGPT-like experience.
- Easily customizable for different use cases (Q&A bot, task assistant, educational bot, etc.).

**How it works:**
1. **Frontend (Streamlit)**:  
   Displays the chat interface, stores message history, and sends all messages to the backend for processing.
2. **Backend (LangGraph)**:  
   Handles conversation flow using a `StateGraph`, processes messages with GPT, and returns AI responses.
3. **OpenAI API**:  
   Powers the AI logic via `ChatOpenAI` for high-quality responses.

---

## 📸 Screenshots
<img width="1265" height="931" alt="image" src="https://github.com/user-attachments/assets/2714c14f-a8af-4c0d-8957-e54871c2c3be" />

---

## 📂 Project Structure
├── backend.py # LangGraph-based chatbot logic
├── frontend.py # Streamlit chat interface
├── .env # Your environment variables (API keys)
└── requirements.txt


---

## ⚙️ Features
- ✅ **Stateful chat** using LangGraph's `InMemorySaver`
- ✅ **OpenAI GPT-powered responses**
- ✅ **Persistent chat history** in a single session
- ✅ **Streamlit chat UI** with markdown rendering
- ✅ Easy to run locally

---

## 🛠 Requirements

- Python 3.10+
- OpenAI API key
- The following Python packages (listed in `requirements.txt`):
  ```txt
  streamlit
  langchain-core
  langchain-openai
  langgraph
  python-dotenv


<img width="1084" height="894" alt="image" src="https://github.com/user-attachments/assets/e931dce2-dc0e-4852-850e-3a69fbc37438" />
<img width="1103" height="412" alt="image" src="https://github.com/user-attachments/assets/d3ee123a-91ba-43e7-a672-2b43f8959180" />

© 2025 Shivendra. All Rights Reserved.




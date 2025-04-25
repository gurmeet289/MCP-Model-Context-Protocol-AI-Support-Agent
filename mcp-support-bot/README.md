# 🧠 MCP Support Bot – Context-Aware AI Agent

This project simulates an **MCP (Model Context Protocol)**-based AI support bot that remembers user history across sessions.

## 🔥 Problem Statement
AI chatbots often **forget what the user said earlier**, making users repeat info.

## ✅ Solution (Using MCP)
We store small "memory chunks" of user interactions with metadata:
- user_id
- issue_type
- message
- plan
- timestamp

Before each LLM call, we:
1. Fetch relevant memory
2. Compose prompt using history
3. Call local Mistral model via Ollama
4. Save new message into memory

## 🛠 Tech Stack
- Streamlit frontend
- Python backend
- JSON as memory store
- Mistral LLM via Ollama (free, open source!)

## 🚀 Run It Locally
```bash
pip install -r requirements.txt
streamlit run app.py

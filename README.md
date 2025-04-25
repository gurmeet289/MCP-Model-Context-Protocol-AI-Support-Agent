# MCP-Model-Context-Protocol-AI-Support-Agent

## 🧠 MCP AI Support Agent
An AI-powered support assistant that uses Model Context Protocol (MCP) to enhance interactions by remembering the context of previous messages and providing more relevant, personalized responses.

## 📘 What is MCP (Model Context Protocol)?
Model Context Protocol (MCP) is a design pattern that enables AI systems to understand the context of a conversation or task, making the model aware of past interactions and enabling context-sensitive responses. By storing and retrieving historical data, MCP helps ensure that each AI response is based on the full context, rather than starting from scratch with every message.

## 🧠 Why MCP Matters

| Without MCP                     | With MCP                              |
|----------------------------------|---------------------------------------|
| “I can't log in again...”        | “I see you’ve had login issues before. Let’s try this…” |
| No history awareness             | Remembers past issues and plans      |
| Repeats answers / no continuity  | Offers more relevant, intelligent responses |
| Lacks empathy or personalization | Offers context-aware, human-like support |


## 💡 Use Cases of MCP
Customer Support: Remember a user's previous support queries for faster resolution.

Virtual Assistants: Track user preferences and tasks for personalized help.

Knowledge Workers: Maintain context in ongoing projects or discussions.

Personalized CRM: Follow up intelligently with clients over time.

## 🛠️ Why Use This Project?

    1) End-to-end MCP pipeline: From memory storage to prompt injection
    
    2) Context-aware support responses based on user history
    
    3) LLM-powered: Uses Mistral model via Ollama
    
    4) Lightweight Streamlit UI: Easy to demo, test, and build upon
    
    5) Modular Codebase: Easily plug in other models or memory formats

## 1) 📁 Project Structure

    mcp-support-bot/
    │
    ├── app.py                   # Streamlit frontend app
    ├── mcp_memory.py            # Handles memory store: load/save/retrieve
    ├── prompt_builder.py        # Builds contextual prompts using memory
    ├── llm_runner.py            # Runs Mistral model via Ollama
    ├── sample_data/
    │   └── memory_store.json    # Stores user interaction memory
    ├── requirements.txt         # Python dependencies
    └── README.md                # Project documentation

## 2)  Installation
    
    I. Clone the repository
          git clone https://github.com/your-username/mcp-support-bot.git
          cd mcp-support-bot
    
    II. (Optional) Create virtual environment
          python -m venv venv
          source venv/bin/activate  # On Windows: venv\Scripts\activate

    III. Install requirements
          pip install -r requirements.txt

    IV. Install and run Ollama + Mistral
          ollama pull mistral

## 3) Running the Bot

      streamlit run app.py
      Go to http://localhost:8501 in your browser.

## 4) 🧪 How It Works
      
      a) User submits a message.
      
      b) The bot stores the message along with context (issue type, user plan, etc.).

      c) The bot retrieves relevant past messages for that user.
      
      d) It builds a prompt that combines the current message with the retrieved memory.
      
      e) The prompt is sent to the LLM (Mistral via Ollama).
      
      f) The bot returns a context-aware response.

## 5) 🧬 Tech Stack

      a) Python 3.8+

      b) Streamlit for the UI

      c) Ollama CLI for running LLMs locally

      d) Mistral 7B as the language model

      e) Simple JSON file as memory store (can be replaced with DB later)

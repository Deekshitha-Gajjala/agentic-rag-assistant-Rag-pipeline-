# 🤖 Agentic RAG Assistant

An intelligent AI assistant that dynamically chooses the best tool to answer user questions.

## Features

* SQL Search for legal cases and company records
* Vector Search (RAG) for regulations and policies
* Web Search for latest news and current events
* General AI for programming and knowledge questions
* LLM-based tool routing using Groq
* Streamlit chat interface

## Architecture

User Query
↓
LLM Router
↓
├── SQL Tool
├── Vector Tool
├── Web Tool
└── General Tool
↓
Response

## Example Questions

* What is Merge Sort?
* Latest AI News
* Amazon privacy lawsuit
* GDPR regulations
* Who is Google's CEO?

## Tech Stack

* Python
* LangChain
* ChromaDB
* Groq API
* Streamlit
* SQLite

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

* Multi-tool reasoning
* Memory
* Conversation history
* Source citations
* Better UI

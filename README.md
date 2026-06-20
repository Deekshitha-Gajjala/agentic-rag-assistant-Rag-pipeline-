# Agentic RAG Assistant

## Overview

Agentic RAG Assistant is an intelligent multi-source AI assistant that combines Retrieval-Augmented Generation (RAG), Vector Search, SQL Querying, and Web Search through an agent-based routing architecture.

Unlike traditional chatbots, the assistant automatically determines the best information source for a user's query and routes requests to specialized tools, enabling more accurate and context-aware responses.

---

## Features

### Intelligent Agent Routing

* Automatically analyzes user queries
* Routes requests to the most appropriate tool
* Supports multiple knowledge sources

### Retrieval-Augmented Generation (RAG)

* Upload PDF documents
* Extract and process document content
* Generate embeddings
* Perform semantic search over uploaded documents

### Vector Database Search

* Store embeddings using vector databases
* Retrieve relevant context for user questions
* Improve response accuracy using RAG

### SQL Database Querying

* Query structured company data
* Retrieve information from relational databases
* Generate natural language responses from SQL results

### Web Search Integration

* Fetch current information from the web
* Handle queries requiring real-time knowledge
* Combine external information with LLM reasoning

### Conversational Interface

* Modern React-based chat interface
* Multi-turn conversation support
* User-friendly interaction experience

---

## System Architecture

```text
User Query
     │
     ▼
Agent Router
     │
 ┌───┼───────────┐
 │   │           │
 ▼   ▼           ▼
RAG SQL       WEB
Tool Tool     Tool
 │   │         │
 └───┴─────────┘
        │
        ▼
     LLM Response
```

---

## Tech Stack

### Frontend

* React.js
* Vite
* JavaScript
* CSS

### Backend

* FastAPI
* Python

### AI & LLM

* Groq API
* Llama Models
* LangChain

### Data Storage

* ChromaDB
* SQLite

### NLP & Embeddings

* HuggingFace Embeddings
* Sentence Transformers

---

## Project Structure

```text
agentic-rag-assistant/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── pages/
│
├── backend/
│   ├── api.py
│   ├── agent.py
│   ├── router.py
│   ├── vector_store.py
│   └── tools/
│
├── uploads/
├── chroma_db/
├── legal_cases.db
└── requirements.txt
```

---

## Workflow

1. User submits a query.
2. Agent Router analyzes intent.
3. Router selects the appropriate tool:

   * Vector Search Tool
   * SQL Tool
   * Web Search Tool
   * General LLM
4. Relevant information is retrieved.
5. Context is passed to the LLM.
6. Response is generated and returned to the user.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Deekshitha-Gajjala/agentic-rag-assistant-Rag-pipeline-.git
cd agentic-rag-assistant-Rag-pipeline-
```

### Backend Setup

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

### Frontend Setup

```bash
npm install
npm run dev
```

---

## API Endpoints

### Health Check

```http
GET /
```

### Chat Endpoint

```http
POST /chat
```

### Upload PDF

```http
POST /upload-pdf
```

---

## Use Cases

* Document Question Answering
* Enterprise Knowledge Assistants
* Legal Document Analysis
* Research Assistance
* Multi-source Information Retrieval
* AI-powered Customer Support

---

## Future Enhancements

* Voice Input
* Voice Responses
* User Authentication
* Chat History Storage
* Multi-PDF Support
* Image Upload & OCR
* Source Citations
* Multi-Agent Collaboration
* Cloud Deployment
* Memory-Augmented Conversations

---

## Contributors

**Deekshitha G**

Computer Science Student | AI & Machine Learning Enthusiast | Generative AI Developer

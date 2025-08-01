# HR Resource Query Chatbot

## Overview

The HR Resource Query Chatbot is an AI-powered tool that helps HR professionals find suitable candidates by parsing natural language queries like:

* "Find Python developers with 3+ years experience"
* "Who has worked on healthcare projects?"
* "Suggest people for a React Native project"

The solution uses a lightweight RAG (Retrieval-Augmentation-Generation) architecture leveraging sentence-transformer embeddings, FAISS for vector search, and a Streamlit frontend to simulate intelligent, human-like responses.

---

## Features

* Semantic search over employee profiles using embeddings
* Natural language query support
* Top-k employee recommendation system
* Instant response via Streamlit chat UI
* Availability-aware results
* Ready for deployment (no API key required)

---

## Architecture

**Components:**

* `sentence-transformers` model: Converts text to vector embeddings
* `FAISS`: Efficient vector similarity search engine
* `Streamlit`: Frontend chat interface
* Employee data (JSON/Python dict): In-memory dataset

**Flow:**

1. Input query from user
2. Query is embedded via transformer model
3. FAISS searches similar employee vectors
4. Response is formatted using the top 3-5 matches

---

## Setup & Installation

### Prerequisites:

* Python 3.8+
* pip

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run locally:

```bash
streamlit run app_streamlit.py
```

---

## API Documentation

(Only if FastAPI backend is implemented)

### POST `/chat`

* Description: Takes a natural language HR query and returns employee matches
* Input: `{ "query": "Find devs with Docker" }`
* Output:

```json
{
  "results": [
    {"name": "Alice Johnson", "skills": ["Python", "Docker"]},
    ...
  ]
}
```

### GET `/employees/search`

* Optional filter-based search API

---

## AI Development Process

* **Tools Used:** ChatGPT (primary assistant), GitHub Copilot (limited)
* **AI Helped With:**

  * Code generation (FAISS, Streamlit, embedding logic)
  * Debugging Python index and search issues
  * Decision support for architecture
* **AI vs Manual:**

  * \~60% of code was AI-assisted
  * \~40% was hand-written or adapted
* **Cool AI Moments:**

  * Auto-building realistic employee samples
  * Helping simplify FAISS integration
* **Limitations:**

  * Error handling logic and Streamlit UI polishing had to be done manually

---

## Technical Decisions

* **Embeddings:** Used `sentence-transformers` (open source, free, local)
* **LLMs:** Chose not to use OpenAI API due to cost and quota limits
* **FAISS vs Cloud Vector DB:** Local FAISS chosen for simplicity and free tier
* **Frontend:** Streamlit selected for fast iteration and deployment
* **Trade-offs:**

  * No true generation step (to avoid API dependency)
  * Limited fallback handling for zero matches

---

## Future Improvements

* Add FastAPI backend with `/chat` endpoint
* Use Ollama + local LLM for natural response generation
* Add resume parser and auto-profile builder
* Allow filtering by availability, location, etc.
* Deploy backend on Railway or Fly.io

---

## Demo

🔗 Live UI: [https://hr-chatbot-gggosaplbwhq7uuh4uocju.streamlit.app/](https://hr-chatbot-gggosaplbwhq7uuh4uocju.streamlit.app/)
📂 GitHub Repo: [https://github.com/sivakrish213/HR-Chatbot](https://github.com/sivakrish213/HR-Chatbot)

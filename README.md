# DocuMind-RAG | HR Policy Assistant

An AI-powered HR Policy Assistant built using Retrieval-Augmented Generation (RAG) that helps employees find accurate answers to company HR policy questions.

The application retrieves relevant information from HR policy documents and uses a Groq-hosted LLM to generate context-aware responses. It integrates safety guardrails to screen user queries and generated answers.

## Overview

Finding relevant information in lengthy HR policy documents can be time-consuming.

DocuMind-RAG simplifies this process by allowing users to ask questions in natural language and receive answers grounded in the HR policy document.

## Features

- Retrieval-Augmented Generation (RAG) pipeline
- PDF/text-based knowledge exploration (verify supported formats)
- Semantic search using Jina embeddings
- Context-aware responses using Groq-hosted LLMs
- Qdrant Cloud vector database integration
- Input and output safety guardrails
- Interactive Streamlit chat interface
- CLI-based interaction
- LangSmith tracing integration

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| LLM Framework | LangChain |
| LLM Provider | Groq |
| Embeddings | Jina |
| Vector Database | Qdrant Cloud |
| Frontend | Streamlit |
| Monitoring | LangSmith |

## Architecture

1. Document Loading
2. Text Chunking
3. Embedding Generation
4. Vector Storage
5. Semantic Retrieval
6. LLM-based Answer Generation
7. Input and Output Safety Validation

## Project Structure

```text
DocuMind-RAG/
├── hr_assistant/
├── data/
├── docs/
├── tests/
├── NOTES/
├── app.py
├── main.py
├── evaluate.py
├── rag.ipynb
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/bhardwajdev046/DocuMind-RAG.git
cd DocuMind-RAG
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

Add the required API keys and configuration:

```env
GROQ_API_KEY=
JINA_API_KEY=
QDRANT_URL=
QDRANT_API_KEY=
QDRANT_COLLECTION_NAME=hr_policy
LANGSMITH_TRACING=false
LANGSMITH_ENDPOINT=
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=
```

Never commit your `.env` file or expose API keys publicly.

### 5. Run the application

For the Streamlit interface:

```bash
streamlit run app.py
```

For the CLI:

```bash
python main.py
```

## Future Improvements

- Support multiple document collections
- Add document upload functionality
- Improve retrieval evaluation
- Add source citations to generated answers
- Enhance conversation memory

## Acknowledgements

This project was adapted from the original
[Basic-Rag repository by d-hackmt](https://github.com/d-hackmt/Basic-Rag).

The original repository served as the starting point for this project.
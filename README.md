# 📄 DocuMind RAG — AI-Powered Document Q&A

DocuMind RAG is an AI-powered document question-answering application built using Retrieval-Augmented Generation (RAG). It allows users to upload PDF documents and ask questions, receiving context-aware answers based on the document's content.

The application also includes an HR Policy Assistant for answering questions about HR policies.

## ✨ Features

- 📄 Upload PDF documents and ask questions.
- 🔍 Semantic search to retrieve relevant document chunks.
- 🤖 AI-generated answers grounded in retrieved content.
- 🏢 Dedicated HR Policy Assistant.
- 🧠 Local embedding model using Sentence Transformers.
- ⚡ In-memory vector store for uploaded documents.
- 💬 Interactive chat interface built with Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| LangChain | RAG pipeline and agent |
| Streamlit | Interactive web interface |
| Groq API | LLM inference |
| HuggingFace Sentence Transformers | Local text embeddings |
| InMemoryVectorStore | Temporary document retrieval |
| Qdrant | HR policy vector storage |
| PyPDF | PDF text extraction |

## 🏗️ Architecture

```text
              User
               |
               v
        Streamlit Interface
               |
       +-------+--------+
       |                |
       v                v
 HR Policy Mode      PDF Q&A Mode
       |                |
       v                v
 Qdrant Store      Upload PDF
       |                |
       |                v
       |           PDF Extraction
       |                |
       |                v
       |          Text Chunking
       |                |
       |                v
       |         Local Embeddings
       |                |
       |                v
       |        In-Memory Vector DB
       |                |
       +-------+--------+
               |
               v
        Semantic Retrieval
               |
               v
           Groq LLM
               |
               v
       Contextual Answer
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/bhardwajdev046/DocuMind-RAG.git
cd DocuMind-RAG
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Ubuntu/Linux**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

Add your API credentials:

```env
GROQ_API_KEY=your_groq_api_key
JINA_API_KEY=your_jina_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
PORTKEY_API_KEY=your_portkey_api_key
```

Never commit your `.env` file or expose API keys publicly.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 🚀 How to Use

1. Launch DocuMind RAG.
2. Select **Chat with PDF** from the sidebar.
3. Upload a PDF document.
4. Enter a question related to the document.
5. Receive an answer based on the retrieved content.

To ask about HR policies, select **HR Policy Assistant**.

## 📂 Project Structure

```text
DocuMind-RAG/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── hr_policy.txt
│   └── sample.pdf
│
└── hr_assistant/
    ├── agent.py
    ├── config.py
    ├── document_loader.py
    ├── embeddings.py
    ├── guardrails.py
    ├── llm.py
    ├── logger.py
    ├── pipeline.py
    ├── splitter.py
    ├── tools.py
    ├── tracing.py
    └── vector_store.py
```

## 🔮 Future Enhancements

- Support multiple PDF uploads.
- Add conversational memory.
- Display document page references in answers.
- Improve retrieval accuracy with hybrid search.
- Add document history and session management.
- Deploy the application to a cloud platform.

## 👨‍💻 Author

**Dev Bhardwaj**

- GitHub: [bhardwajdev046](https://github.com/bhardwajdev046)
- LinkedIn: [Dev Bhardwaj](https://www.linkedin.com/in/dev-bhardwaj-23338a294)

---

Built with Python, LangChain, and RAG.
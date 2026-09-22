"""Wires all components into a ready-to-use RAG assistant."""

from pathlib import Path

from langchain_core.vectorstores import InMemoryVectorStore

from hr_assistant import config
from hr_assistant.agent import create_hr_agent, create_document_agent
from hr_assistant.document_loader import load_document
from hr_assistant.llm import get_llm
from hr_assistant.splitter import split_into_chunks
from hr_assistant.tools import create_search_tool
from hr_assistant.guardrails import (
    REFUSAL_MESSAGE,
    check_input,
    check_output,
)
from hr_assistant.vector_store import (
    build_vector_store,
    get_retriever,
    load_vector_store,
    vector_store_exists,
)
from hr_assistant.embeddings import get_embeddings_model
from hr_assistant.tracing import check_langsmith_tracing
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def build_vector_store_for_document(file_path: str = config.DATA_FILE_PATH):
    """Build or reuse the default HR policy Qdrant vector store."""

    if vector_store_exists():
        logger.info("Reusing existing Qdrant HR policy collection")
        return load_vector_store()

    documents = load_document(file_path)
    chunks = split_into_chunks(documents)

    return build_vector_store(chunks)


def build_temporary_vector_store(file_path: str):
    """Build an isolated in-memory vector store for an uploaded document."""

    documents = load_document(file_path)
    chunks = split_into_chunks(documents)

    if not chunks:
        raise ValueError("No readable text found in the uploaded document.")

    embeddings = get_embeddings_model()

    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(chunks)

    logger.info(
        "Created temporary vector store with %d chunks from %s",
        len(chunks),
        file_path,
    )

    return vector_store


def build_hr_assistant(file_path: str = config.DATA_FILE_PATH):
    """Build the default HR policy RAG assistant."""

    config.check_api_keys()
    check_langsmith_tracing()

    vector_store = build_vector_store_for_document(file_path)
    retriever = get_retriever(vector_store)

    search_tool = create_search_tool(retriever)
    llm = get_llm()

    return create_hr_agent(llm, [search_tool])


def build_document_assistant(file_path: str):
    """Build a RAG assistant for an uploaded TXT or PDF document."""

    config.check_api_keys()
    check_langsmith_tracing()

    vector_store = build_temporary_vector_store(file_path)
    retriever = get_retriever(vector_store)

    search_tool = create_search_tool(retriever)
    llm = get_llm()

    return create_document_agent(llm, [search_tool])


def ask(agent, question: str) -> str:
    """Ask the RAG agent a question and return its answer."""

    input_is_safe, _ = check_input(question)

    if not input_is_safe:
        return REFUSAL_MESSAGE

    response = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )

    answer = response["messages"][-1].content

    output_is_safe, _ = check_output(answer)

    if not output_is_safe:
        return REFUSAL_MESSAGE

    return answer

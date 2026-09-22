"""Local HuggingFace embeddings for the RAG pipeline."""

from langchain_huggingface import HuggingFaceEmbeddings

from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def get_embeddings_model():
    """Return a local sentence-transformer embedding model."""

    model_name = "sentence-transformers/all-MiniLM-L6-v2"

    logger.info("Initializing local embeddings model: %s", model_name)

    return HuggingFaceEmbeddings(
        model_name=model_name
    )

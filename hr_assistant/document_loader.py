"""Load raw TXT or PDF documents for the RAG pipeline."""

from pathlib import Path

from langchain_community.document_loaders import TextLoader, PyPDFLoader

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def load_document(file_path: str = config.DATA_FILE_PATH):
    """Load a .txt or .pdf file and return LangChain Document objects."""

    path = Path(file_path)
    logger.info("Loading document from '%s'", file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {file_path}")

    suffix = path.suffix.lower()

    if suffix == ".txt":
        loader = TextLoader(str(path), encoding="utf-8")

    elif suffix == ".pdf":
        loader = PyPDFLoader(str(path))

    else:
        raise ValueError(
            f"Unsupported file format: {suffix}. Use .txt or .pdf."
        )

    documents = loader.load()

    logger.info("Loaded %d document(s)", len(documents))

    return documents
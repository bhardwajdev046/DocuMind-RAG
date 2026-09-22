"""Connect directly to Groq LLM."""

from langchain_groq import ChatGroq

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def get_llm():
    """Return a Groq chat model."""
    logger.info("Initializing LLM via Groq")

    return ChatGroq(
        model=config.LLM_MODEL_NAME,
        temperature=0,
    )

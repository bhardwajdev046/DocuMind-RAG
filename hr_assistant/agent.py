"""Build agents for HR policy and general document Q&A."""

from langchain.agents import create_agent

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def create_hr_agent(llm, tools):
    """Create an HR policy assistant."""

    logger.info("Creating HR agent with %d tool(s)", len(tools))

    return create_agent(
        model=llm,
        tools=tools,
        system_prompt=config.SYSTEM_PROMPT,
    )


def create_document_agent(llm, tools):
    """Create a general-purpose document Q&A assistant."""

    logger.info("Creating document agent with %d tool(s)", len(tools))

    return create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are a helpful document question-answering assistant. "
            "Use the document search tool to find information relevant to "
            "the user's question. Answer clearly based on the retrieved "
            "document content. If the answer is not present in the document, "
            "say that you could not find it. Do not invent information."
        ),
    )

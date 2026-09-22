"""Wrap the retriever as a generic document search tool."""

from langchain.tools import tool

from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def create_search_tool(retriever, tool_name="search_document"):
    """Create a search tool for the provided document."""

    @tool(tool_name)
    def search_document(question: str) -> str:
        """Search the uploaded document for information relevant to the user's question."""

        logger.info("Document search called with query: %s", question)

        matching_chunks = retriever.invoke(question)

        logger.info("Found %d matching chunks", len(matching_chunks))

        if not matching_chunks:
            return "No relevant information found in the document."

        return "\n\n".join(chunk.page_content for chunk in matching_chunks)

    return search_document

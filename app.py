"""Streamlit app for HR Policy and PDF Document Q&A."""

import streamlit as st
import tempfile
import os

from hr_assistant.logger import get_logger
from hr_assistant.pipeline import (
    ask,
    build_hr_assistant,
    build_document_assistant,
)

logger = get_logger(__name__)

st.set_page_config(page_title="DocuMind RAG", page_icon="📄")
st.title("📄 DocuMind RAG")
st.caption("Ask questions about HR policies or upload your own PDF.")

# Existing HR Policy Assistant
@st.cache_resource(show_spinner="Setting up HR assistant...")
def get_hr_agent():
    return build_hr_assistant()


# PDF Assistant
@st.cache_resource(show_spinner="Processing PDF...")
def get_pdf_agent(file_path, file_name):
    return build_document_assistant(file_path)


mode = st.sidebar.radio(
    "Choose Assistant",
    ["Chat with PDF", "HR Policy Assistant"]
)

if mode == "HR Policy Assistant":
    st.subheader("🤖 HR Policy Assistant")
    agent = get_hr_agent()

else:
    st.subheader("📑 Chat with your PDF")

    uploaded_file = st.file_uploader(
        "Upload a PDF document",
        type=["pdf"]
    )

    if uploaded_file:
        # Save uploaded PDF temporarily
        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"Uploaded: {uploaded_file.name}")

        try:
            agent = get_pdf_agent(file_path, uploaded_file.name)
        except Exception as e:
            st.error(f"Could not process PDF: {e}")
            st.stop()

    else:
        st.info("Upload a PDF to start asking questions.")
        st.stop()


# Chat history per assistant mode
chat_key = f"messages_{mode}"

if chat_key not in st.session_state:
    st.session_state[chat_key] = []

for message in st.session_state[chat_key]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input("Ask your question...")

if question:
    st.session_state[chat_key].append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask(agent, question)
        st.markdown(answer)

    st.session_state[chat_key].append(
        {"role": "assistant", "content": answer}
    )

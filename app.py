import streamlit as st
from agent import run_agent
from tools.pdf_tool import extract_pdf_text

st.set_page_config(
    page_title="Agentic RAG Assistant",
    page_icon="🤖"
)

st.title("🤖 Agentic RAG Assistant")

# STEP 3
uploaded_pdf = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# STEP 4
pdf_text = ""

if uploaded_pdf:
    pdf_text = extract_pdf_text(uploaded_pdf)
    st.success("PDF uploaded successfully!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask a question")
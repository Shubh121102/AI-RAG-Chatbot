import streamlit as st
from rag import extract_text_from_pdf, create_faiss_vector_store, build_qa_chain
import os

# Sidebar for file upload
st.sidebar.title("Upload your PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

# Title and description in the center
st.title("AI RAG Chatbot")
st.write("Upload a PDF from the sidebar and ask questions based on its content.")

# Handle uploaded file
if uploaded_file is not None:
    pdf_path = f"uploaded/{uploaded_file.name}"
    os.makedirs("uploaded", exist_ok=True)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text_from_pdf(pdf_path)

    st.info("Creating FAISS vector store...")
    create_faiss_vector_store(text)

    st.info("Initializing chatbot...")
    qa_chain = build_qa_chain()
    st.success("Chatbot is ready!")

# Chatbox area in the center
if 'qa_chain' in locals():
    st.markdown("---")
    question = st.text_input("Ask a question about the uploaded PDF:")
    if question:
        st.info("Querying the document...")
        answer = qa_chain.run(question)
        st.success(f"Answer: {answer}")

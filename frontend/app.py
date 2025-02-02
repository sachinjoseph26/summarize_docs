import sys
import os


# Ensure backend module is discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
from backend.document_processing import extract_text
from backend.agents import summarize_text, ask_question


# Create an "uploads" folder if it doesn't exist
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("📄 AI Document Summarization & Q&A")

uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "txt", "docx"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    # Save file to "uploads/" with correct name and extension
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.write(f"✅ File saved at: {file_path}")  # Debugging

    # Extract Text
    with st.spinner("Extracting text..."):
        document_text = extract_text(file_path)

    st.subheader("📜 Extracted Text Preview")
    st.write(document_text[:1000] + "...")  # Show first 1000 characters

    # Summarization
    if st.button("Summarize Document"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(document_text)
        st.subheader("📌 Document Summary")
        st.write(summary)

    # Q&A Input Box
    user_question = st.text_input("Ask a question about the document:")

    if user_question:
        with st.spinner("Fetching answer..."):
            answer = ask_question(document_text, user_question)
        st.subheader("💡 AI Answer")
        st.write(answer)

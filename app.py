import streamlit as st
from PyPDF2 import PdfReader

# Set the title and layout of the Streamlit app
st.set_page_config(page_title="Chat & PDF Viewer", layout="wide")

# Sidebar for uploading documents
with st.sidebar:
    st.title("Upload Documents")
    uploaded_pdf = st.file_uploader("Upload your PDF", type=["pdf"])

# Main page layout
col1, col2 = st.columns(2)

# Column 1: Chat Interface
with col1:
    st.title("Chat Interface")
    user_input = st.text_input("Type your message here")
    if user_input:
        # Process the chat input here
        st.write(f"You said: {user_input}")

        # Display a placeholder for chat responses
        st.write("Chat response will appear here")

# Column 2: PDF Rendering
with col2:
    st.title("PDF Viewer")
    if uploaded_pdf is not None:
        # Display the PDF
        pdf_reader = PdfReader(uploaded_pdf)
        raw_text = ""
        for page in pdf_reader.pages:
            raw_text += page.extract_text() + "\n"

        # Render the PDF text
        st.text(raw_text)
        # Alternatively, display the PDF using st.download_button for downloading or st.write for a visual preview

import streamlit as st
import base64
from PyPDF2 import PdfReader
import os

# Set the title and layout of the Streamlit app
st.set_page_config(page_title="Chat & PDF Viewer", layout="wide")


# Helpers
def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="overflow: auto; width: 100%; height: 800px;">"""

    st.markdown(pdf_display, unsafe_allow_html=True)


# Sidebar for uploading documents
with st.sidebar:
    st.title("Upload Documents")
    uploaded_pdf = st.file_uploader("Upload your PDF", type=["pdf"])

# Main page layout
col1, col2 = st.columns([4, 5], gap="small")

# Column 1: Chat Interface
with col1:
    st.title("Chat Interface")
    user_input = st.text_input("Type your message here")
    if user_input:
        st.write(f"You said: {user_input}")
        st.write("Chat response will appear here")


# Column 2: PDF Rendering
with col2:
    st.title("PDF Viewer")

    if uploaded_pdf is not None:
        with open("temp_pdf.pdf", "wb") as f:
            f.write(uploaded_pdf.getbuffer())

        displayPDF("temp_pdf.pdf")
        # os.remove("temp_pdf.pdf") # Uncomment to delete the temp file after rendering
    else:
        displayPDF("medicaid.pdf")

import streamlit as st
import base64
from PyPDF2 import PdfReader
import random

# Set the title and layout of the Streamlit app
st.set_page_config(page_title="Chat & PDF Viewer", layout="wide")

document_data = {
    "mandatory_documents": {
        "Driver's ID / State ID": "🆔",
        "Proof of Residence": "🏠",
        "Birth Certificate": "📄",
        "Social Security Card": "💳",
        "Bank Statements": "🏦",
        "Pay Stubs": "🧾",
    },
    "optional_documents": {
        "Veteran Papers": "🎖️",
        "Income Tax Returns": "📊",
        "Proof of Pregnancy": "🤰",
        "Lease Agreement": "🏘️",
        "Tax Returns": "📋",
        "Family Certificates": "👨‍👩‍👧‍👦",
        "Vehicle Registration": "🚗",
        "Utility Bills": "💡",
        "Employment Records": "💼",
    },
}


# Placeholder function to simulate document assessment
def assess_document(uploaded_file):
    # TODO: In a real scenario, this function would send the file to GPT-4 or another service
    all_docs = list(document_data["mandatory_documents"].keys()) + list(
        document_data["optional_documents"].keys()
    )
    # For now, it returns a random document type from the combined list.
    # return random.choice(all_docs)
    return all_docs[0]


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
    uploaded_file = st.file_uploader(
        "Upload your documents", type=["pdf", "jpg", "png", "docx"]
    )

    if uploaded_file is not None:
        # Document Assessment
        doc_type = assess_document(uploaded_file)
        st.write(f"Uploaded document is identified as: {doc_type}")

        # Update the status of the uploaded document
        if doc_type in document_data["mandatory_documents"]:
            document_data["mandatory_documents"][doc_type] = "✅"
        elif doc_type in document_data["optional_documents"]:
            document_data["optional_documents"][doc_type] = "✅"

    # Displaying mandatory documents with their current status
    st.markdown("### Mandatory Documents")
    for doc, emoji in document_data["mandatory_documents"].items():
        if emoji == "✅":
            st.markdown(f"* **{emoji} {doc}**")  # Bold if the document is uploaded
        else:
            st.markdown(f"* {emoji} {doc}")

    # Displaying optional documents with their current status
    st.markdown("### Optional Documents")
    for doc, emoji in document_data["optional_documents"].items():
        if emoji == "✅":
            st.markdown(f"* **{emoji} {doc}**")  # Bold if the document is uploaded
        else:
            st.markdown(f"* {emoji} {doc}")


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

    if uploaded_file is not None:
        # TODO: Update the logic to render the medicaid form as we fill it out.
        # theoretically here it is not about uploaded file but the re-rendered pdf. Anyhow, leaving the logic for demo.
        with open("temp_pdf.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        displayPDF("temp_pdf.pdf")
        # os.remove("temp_pdf.pdf") # Uncomment to delete the temp file after rendering
    else:
        displayPDF("medicaid.pdf")

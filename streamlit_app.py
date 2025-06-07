import streamlit as st
import fitz
import requests

# Function definitions go here, at the top
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    return "".join(page.get_text() for page in doc)

def summarize_with_api(text, token):
    url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"inputs": text[:1000]}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]['summary_text']
    return f"Error: {response.status_code}"

# Streamlit UI code below
st.title("📄 AI Legal Document Summarizer")
st.write("App Loaded Successfully!")  # Debug message

pdf_file = st.file_uploader("Upload your legal PDF", type=["pdf"])
api_key = st.text_input("Enter your Hugging Face API key", type="password")

if st.button("Summarize"):
    st.write("Summarize button clicked")  # Debug message
    if not pdf_file:
        st.error("Please upload a PDF file!")
    elif not api_key:
        st.error("Please enter your API key!")
    else:
        with st.spinner("Extracting and summarizing..."):
            text = extract_text_from_pdf(pdf_file)
            summary = summarize_with_api(text, api_key)
            st.subheader("🔍 Summary")
            st.write(summary)

            with open("summary.txt", "w", encoding="utf-8") as f:
                f.write(summary)
            st.success("✅ Summary saved to summary.txt")

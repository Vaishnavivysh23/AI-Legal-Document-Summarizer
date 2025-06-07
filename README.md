# AI-Legal-Document-Summarizer
AI Legal Document Summarizer is a simple yet powerful tool built using Python and Streamlit that allows users to upload lengthy legal or government documents (PDFs) and generate concise, easy-to-read summaries using an AI model.
## 🚀 Features

- Upload legal or government PDF documents.
- Extract text directly from PDFs using **PyMuPDF**.
- Generate AI-powered summaries by calling the Hugging Face `facebook/bart-large-cnn` model via API.
- User-friendly web interface with Streamlit.
- Saves the summary as a local text file (`summary.txt`).

---

## 🛠️ Technology Stack

- Python
- Streamlit (for the web interface)
- PyMuPDF (`fitz`) (to extract text from PDF)
- Requests (to interact with Hugging Face API)

---

## 📋 Getting Started

### Prerequisites

- Python 3.7 or higher installed.
- A Hugging Face API key (Get one by creating a free account on [Hugging Face](https://huggingface.co/) and generating an access token).

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/ai-legal-document-summarizer.git
    cd ai-legal-document-summarizer
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

```bash

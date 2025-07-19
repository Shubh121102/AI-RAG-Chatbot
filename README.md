# AI-RAG-Chatbot🧠  - PDF Query using RAG (Retrieval-Augmented Generation)

This project is an AI-powered chatbot that allows users to upload any PDF file and interactively **query its content**. It uses the **RAG (Retrieval-Augmented Generation)** architecture to combine information retrieval and LLM-based response generation.

Built with:
- 🧠 LLMs (via HuggingFace / OpenAI)
- 📄 PDF parsing
- 🔍 Vector search
- 🌐 Streamlit frontend for interactive UI

---

## 📁 Project Structure

```
📦 your-project/
├── rag.py              # Core RAG logic: chunking, embeddings, retrieval, LLM
├── app.py              # Streamlit UI for file upload & chat interface
├── .env                # Environment variables (API keys, config)
├── requirements.txt    # Python dependencies
├── myenv-venv/         # Virtual environment (not uploaded to GitHub)
└── README.md           # This file
```

---

## 🚀 How It Works

1. **PDF Upload**: User uploads a PDF file via Streamlit UI.
2. **Chunking & Embeddings**: The file is chunked and converted into vector embeddings.
3. **Retrieval**: When a query is made, relevant chunks are retrieved using vector similarity.
4. **Generation**: The retrieved context is passed to a language model to generate an accurate answer.

---

## 💻 Installation & Setup


### 1. Create a Virtual Environment

```bash
python -m venv myenv-venv
source myenv-venv/bin/activate  # On Windows: myenv-venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file in the root directory with your credentials (example):

```
OPENAI_API_KEY=your_key_here
# or HUGGINGFACE_API_KEY=...
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open the URL shown in the terminal (typically http://localhost:8501) to interact with the chatbot.

---

## 🛠 Tech Stack

- **Streamlit** — for building the frontend UI
- **LangChain or FAISS** — for chunking and vector similarity search
- **PyPDF** — for PDF parsing
- **Gemini or HuggingFace LLMs** — for generating answers
- **dotenv** — for managing secret keys

---

## 📌 Features

- Upload and parse any PDF file
- Chunk and embed content using vector databases
- Ask context-aware questions
- Clean and simple Streamlit UI

---

## 📷 Screenshot (Optional)

<img width="947" height="440" alt="Screenshot 2025-07-19 165455" src="https://github.com/user-attachments/assets/c2e5350d-8643-44bb-88ca-2f1f1a6caa3c" />
<img width="953" height="429" alt="Screenshot 2025-07-19 165550" src="https://github.com/user-attachments/assets/8ea708be-cb90-416d-be1f-c41cd53d663a" />

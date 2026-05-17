# 📄 RAG PDF Chat Application

A Retrieval-Augmented Generation (RAG) based application that allows users to upload PDFs and chat with their documents using AI.

This project uses:
- FastAPI for backend
- HTML, CSS, JavaScript for frontend
- Docker for containerization

---

# 🚀 Features

✅ Upload PDF documents  
✅ Chat with PDF content  
✅ Semantic search using RAG  
✅ FastAPI backend APIs  
✅ Responsive UI using HTML & CSS  
✅ Docker support  
✅ AI-powered question answering  

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI
- Python

## AI / RAG
- PDF Text Extraction
- Embedding Model
- Vector Database
- LLM Integration

## Deployment
- Docker

---

# 📁 Project Structure

```bash
rag-pdf-chat/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── ...
│
├── uploads/
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rag-pdf-chat.git
cd rag-pdf-chat
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

## Start FastAPI Server

```bash
uvicorn main:app --reload
```

Application runs on:

```bash
http://127.0.0.1:8000
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t rag-pdf-chat .
```

## Run Docker Container

```bash
docker run -p 8000:8000 rag-pdf-chat
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload PDF |
| POST | `/chat` | Chat with PDF |
| GET | `/` | Home Route |

---

# 🧠 How RAG Works

1. Upload PDF document  
2. Extract text from PDF  
3. Convert text into embeddings  
4. Store embeddings in vector database  
5. Retrieve relevant chunks  
6. Generate AI response using LLM  

---

# 🎯 Use Cases

- Research Assistant
- PDF Question Answering
- Study Assistant
- Document Analysis
- AI Knowledge Base

---

# 🔮 Future Improvements

- Multiple PDF support
- Authentication
- Chat history
- Better UI/UX
- Cloud deployment

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository and submit pull requests.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed by **Ankit Virat**

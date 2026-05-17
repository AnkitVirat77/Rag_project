# =========================
# 1. IMPORTS (FIXED)
# =========================
import os
from dotenv import load_dotenv

from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from pinecone import Pinecone, ServerlessSpec

# =========================
# 2. LOAD API KEYS (FIXED)
# =========================
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# =========================
# 3. LOAD & SPLIT PDF (FIXED PATH)
# =========================
loader = PyPDFLoader(
    r"C:\Users\HP\Documents\Nareshit\GenAI\New folder\SBI-Clerk-Prelims-Syllabus-2024.pdf"
)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)

# =========================
# 4. EMBEDDINGS
# =========================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# 5. PINECONE SETUP
# =========================
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "multi-query-rag-index"

existing_indexes = [i.name for i in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

vectorstore = PineconeVectorStore.from_documents(
    docs,
    embeddings,
    index_name=index_name
)

# =========================
# 6. LLM (GROQ)
# =========================
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.1,
    groq_api_key=GROQ_API_KEY
)

# =========================
# 7. RAG CHAIN
# =========================
system_prompt = (
    "Use the given context to answer the question. "
    "If you don't know the answer, say you don't know. "
    "Context: {context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

qa_chain = create_stuff_documents_chain(llm, prompt)

rag_chain = create_retrieval_chain(
    vectorstore.as_retriever(),
    qa_chain
)

# =========================
# 8. TEST
# =========================
query = "What is the main topic of the uploaded PDF?"

response = rag_chain.invoke({"input": query})

query = "How Many people developed the Transformers Model according to the PDF"
response = rag_chain.invoke({"input": query})
print(response['answer'])



print("\nQ:", query)
print("A:", response["answer"])
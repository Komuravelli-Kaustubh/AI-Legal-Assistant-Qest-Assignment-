import os
import pickle
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from modules.config import PDF_FOLDER, PKL_FILE

def load_or_create_faiss():
    """Loads FAISS from pickle or creates it from PDFs if not found."""
    if os.path.exists(PKL_FILE):
        print("✅ Loading FAISS from pickle file...")
        with open(PKL_FILE, "rb") as f:
            return pickle.load(f)

    print("🔄 No FAISS found. Processing PDFs...")
    pdf_files = [os.path.join(PDF_FOLDER, f) for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
    documents = []
    
    for pdf in pdf_files:
        loader = PyPDFLoader(pdf)
        documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(texts, embedding_model)

    with open(PKL_FILE, "wb") as f:
        pickle.dump(vector_db, f)
    
    print("✅ FAISS index created & saved!")
    return vector_db

# Load FAISS vector store
vector_db = load_or_create_faiss()

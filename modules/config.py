import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

PHI_API_KEY = os.getenv("PHI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PDF_FOLDER = "data/pdfs" #pdfs path
PKL_FILE = "data/faiss_index.pkl" #pickle path of pdfs FAISS index file

# 🚀 AI-Powered Legal Chatbot: Intelligent Legal Information Retrieval System

## 📌 Project Overview
The **AI-Powered Legal Chatbot** is an advanced system that retrieves, analyzes, and summarizes legal documents efficiently. It uses **FAISS for vector search, LangChain for text processing, Phi Agents for multi-agent coordination, and Groq AI for summarization**. This chatbot allows users to query legal information and receive **relevant legal text along with simplified summaries**.

### **🔹 Use Case**
📜 Legal professionals, law students, and researchers can quickly find legal references, analyze them, and get AI-driven simplified explanations without manually searching through legal documents.

### **🔹 How It Solves the Problem**
- Automates legal text retrieval from **uploaded PDFs**.
- Uses **vector embeddings & FAISS** for **efficient similarity search**.
- **Summarizes complex legal jargon** into **simpler terms** using **Groq AI**.
- **Remembers chat history** to maintain context in conversations.

---

## 🛠️ Tech Stack
| **Technology**      | **Purpose** |
|---------------------|------------|
| **Python**         | Core Programming Language |
| **Streamlit**      | Web UI Framework |
| **FAISS**          | Vector Store for Fast Retrieval |
| **LangChain**      | NLP Processing & Query Handling |
| **Hugging Face**   | Sentence Embeddings |
| **Groq AI**        | AI-Based Summarization |
| **Phi Agents**     | Multi-Agent System for Coordination |
| **dotenv**         | Environment Variable Management |

---

## 🔧 Installation & Setup

### **1️⃣ Clone the Repository**
git clone https://github.com/your-username/AI-Legal-Chatbot.git
cd AI-Legal-Chatbot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set Up API Keys
Create a .env file in the root directory and add:
PHI_API_KEY="your-phi-api-key"
GROQ_API_KEY="your-groq-api-key"
If deploying on Streamlit Cloud, add the same keys in .streamlit/secrets.toml:
PHI_API_KEY = "your-phi-api-key"
GROQ_API_KEY = "your-groq-api-key"
4️⃣ Run the Application
streamlit run app.py
✅ Open your browser at http://localhost:8501

🧠 How It Works
📌 1️⃣ Data Processing & Storage
✔ Checks for an existing FAISS vector store (Pickle file).
✔ If found, it loads the FAISS index.
✔ If not found, it processes PDFs → text → vector embeddings and saves them.

📌 2️⃣ AI-Powered Query Handling
✔ Uses Phi Agents for multi-agent collaboration.
✔ QueryAgent fetches relevant legal text using FAISS.
✔ SummarizationAgent simplifies legal jargon into easy-to-understand text.

📌 3️⃣ Chatbot Interface
✔ Built with Streamlit for an interactive UI.
✔ Users input queries, AI retrieves legal text, and AI simplifies the answer.
✔ Supports conversational history for context-aware responses.

🎯 Key Features
✅ Retrieves Legal Text – AI fetches legal references using vector search.
✅ AI Summarization – Converts complex legal terms into simple explanations.
✅ Multi-Agent System – Uses specialized AI agents for different tasks.
✅ Persistent Data Storage – Saves embeddings in FAISS for fast future searches.
✅ Web-Based UI – Accessible via Streamlit, no local setup needed.

📌 Future Enhancements
🔹 Add Voice Query Support – Convert speech to text for hands-free legal queries.
🔹 Expand Legal Database – Add more legal documents from multiple sources.
🔹 Multi-Language Support – Enable AI-generated legal summaries in different languages.

👨‍💻 Developed By
🚀 Komuravelli Kaustubh
🔗 GitHub: github.com/Komuravelli-Kaustubh
📧 Contact: shankarkaustubh1k3@gmail.com

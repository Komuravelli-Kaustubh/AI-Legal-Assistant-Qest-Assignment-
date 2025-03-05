import groq
from phi.agent import Agent
from phi.model.groq import Groq
from modules.config import GROQ_API_KEY
from modules.faiss_handler import vector_db

# **🔹 Retrieve Legal Text**
def retrieve_legal_text(query: str):
    """Fetch relevant legal sections from FAISS DB."""
    docs = vector_db.similarity_search(query, k=2)
    return "\n\n".join([doc.page_content for doc in docs])

# **🔹 Summarize Legal Text**
def summarize_legal_text(text: str):
    """Summarizes legal text into easy-to-understand language."""
    prompt = f"Summarize the following legal information in simple terms:\n\n{text}"
    response = groq.Client(api_key=GROQ_API_KEY).chat.completions.create(
        model="mixtral",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# **🔹 Query Agent**
query_agent = Agent(
    name="QueryAgent",
    role="Legal Information Retriever",
    model=Groq(id="llama3-8b-8192"),
    tools=[retrieve_legal_text],
    instructions="Retrieve legal data from FAISS."
)

# **🔹 Summarization Agent**
summarization_agent = Agent(
    name="SummarizationAgent",
    role="Legal Text Simplifier",
    model=Groq(id="llama3-8b-8192"),
    tools=[summarize_legal_text],
    instructions="Summarize legal text for users."
)

# **🔹 Multi-Agent System**
multi_ai_agent = Agent(
    team=[query_agent, summarization_agent],
    name="MultiAgent",
    model=Groq(id="llama3-8b-8192"),
    instructions="Retrieve legal data and summarize it.",
    show_tool_calls=True,
    markdown=True
)

# **🔹 Multi-Agent Chatbot Class**
class MultiAgentChatbot:
    def __init__(self):
        self.chat_history = []
        self.multi_ai_agent = multi_ai_agent

    def chat(self, user_input):
        """Process user query with AI and maintain chat history."""
        self.chat_history.append({"role": "user", "content": user_input})
        response = groq.Client(api_key=GROQ_API_KEY).chat.completions.create(
            model="llama3-8b-8192",
            messages=self.chat_history
        )
        bot_response = response.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": bot_response})
        return bot_response

# **🔹 Initialize Chatbot**
chatbot = MultiAgentChatbot()

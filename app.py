import streamlit as st
from modules.chatbot import chatbot  

st.set_page_config(page_title="⚖️ AI Legal Chatbot", page_icon="⚖️")

st.title("⚖️ AI-Powered Legal Chatbot")
st.write("**Ask legal questions and get AI-generated responses based on stored legal documents.**")

# **🔹 User Input Box**
user_input = st.text_input("📜 Enter your legal query:")

# **🔹 Process Query**
if st.button("🔍 Submit"):
    if user_input:
        with st.spinner("📖 Fetching legal info..."):
            response = chatbot.chat(user_input)
        st.subheader("💡 AI-Powered Response:")
        st.write(response)
    else:
        st.warning("⚠️ Please enter a legal question.")

# **🔹 Footer**
# 🔹 Footer Section
st.markdown("---")  
st.markdown(
    """
    <div style="text-align: center;">
        <h4>🚀 AI-Powered Legal Chatbot</h4>
        <p style="font-size: 14px;">
            Enhancing legal research with advanced AI-driven insights.
        </p>
        <p style="font-size: 14px;">
            Built using <b>Phi Agents, Groq AI, LangChain & FAISS</b>
        </p>
        <hr style="border: none; height: 1px; background: #ccc;">
        <p style="font-size: 14px; color: #777;">
            Developed by <b>Komuravelli Kaustubh</b>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

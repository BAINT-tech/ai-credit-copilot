import streamlit as st
import google.generativeai as genai

# -------------------------------
# 💳 AI Credit Copilot — Gemini Edition (Fixed)
# -------------------------------

st.set_page_config(page_title="💳 AI Credit Copilot", page_icon="💳")

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit using credit capilot AI.")

# 🔑 Gemini API Key
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", "")

if not GOOGLE_API_KEY:
    st.warning("⚠️ Please add your Google API key in Streamlit Secrets as 'GOOGLE_API_KEY'.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash-latest")  # 👈 Updated model name

# 🧠 User Input
credit_question = st.text_input("Enter your credit-related question:")

# 🚀 Run AI
if st.button("Ask Copilot"):
    if not GOOGLE_API_KEY:
        st.error("Missing API key. Add it in Streamlit Secrets.")
    elif not credit_question.strip():
        st.error("Please type a question before clicking 'Ask Copilot'.")
    else:
        with st.spinner("💭 Thinking..."):
            try:
                response = model.generate_content(credit_question)
                st.success("✅ Here's what I found:")
                st.write(response.text)
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")

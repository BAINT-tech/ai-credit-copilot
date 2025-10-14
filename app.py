import streamlit as st
import google.generativeai as genai
import os

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit with Capilot AI (auto fallback enabled).")

# Load your Gemini API key
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Define models
PRIMARY_MODEL = "gemini-2.5-pro-preview-03-25"
FALLBACK_MODEL = "gemini-1.5-flash"

def generate_answer(question):
    """Try the main model, fallback to a lighter one if quota or error occurs."""
    try:
        model = genai.GenerativeModel(PRIMARY_MODEL)
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        if "quota" in str(e).lower() or "429" in str(e):
            st.warning("⚠️ Pro model quota reached — switching to fallback model...")
            try:
                model = genai.GenerativeModel(FALLBACK_MODEL)
                response = model.generate_content(question)
                return response.text
            except Exception as e2:
                return f"⚠️ Both models unavailable. Error: {e2}"
        return f"⚠️ Error: {e}"

# User input
user_question = st.text_input("Enter your credit-related question:")
if st.button("Ask AI"):
    if user_question.strip():
        with st.spinner("Thinking..."):
            answer = generate_answer(user_question)
        st.success("✅ Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question first.")

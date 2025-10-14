import streamlit as st
import google.generativeai as genai

# Load your Google API key safely
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="💳 AI Credit Copilot", page_icon="💳")
st.title("💳 AI Credit Copilot")
st.caption("Get AI-powered guidance to improve and manage your credit using Google Gemini AI.")

# Input box
question = st.text_input("Enter your credit-related question:")

# Button action
if st.button("Ask AI"):
    if not question.strip():
        st.warning("Please type a question first.")
    else:
        try:
            # Use a supported Gemini model
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(question)

            st.success("✅ Here's Gemini's advice:")
            st.write(response.text)

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

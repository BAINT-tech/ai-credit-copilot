import streamlit as st
import google.generativeai as genai

# Load your Google API key from Streamlit secrets
api_key = st.secrets["GOOGLE_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# App UI
st.set_page_config(page_title="💳 AI Credit Copilot", page_icon="💳")
st.title("💳 AI Credit Copilot")
st.caption("Get AI-powered guidance to improve and manage your credit with Google Gemini AI.")

# User input
question = st.text_input("Enter your credit-related question:")

# When user asks a question
if st.button("Ask AI"):
    if question.strip() == "":
        st.warning("Please enter a question first.")
    else:
        try:
            # Use Gemini 1.5 model
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(question)

            # Display the answer
            st.success("✅ Here’s what Gemini suggests:")
            st.write(response.text)

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

import streamlit as st
import google.generativeai as genai

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit with credit Capilot AI (auto fallback enabled).")

# Load your Gemini API key securely
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Correct model IDs for the new API
PRIMARY_MODEL = "gemini-1.5-pro-latest"
FALLBACK_MODEL = "gemini-1.5-flash-latest"

def generate_answer(question):
    try:
        model = genai.GenerativeModel(PRIMARY_MODEL)
        response = model.generate_content(question)
        return f"🧠 Model: {PRIMARY_MODEL}\n\n{response.text}"
    except Exception as e:
        if "quota" in str(e).lower() or "429" in str(e) or "404" in str(e):
            st.warning("⚠️ Pro model not available — switching to fallback model...")
            try:
                model = genai.GenerativeModel(FALLBACK_MODEL)
                response = model.generate_content(question)
                return f"⚡ Model: {FALLBACK_MODEL}\n\n{response.text}"
            except Exception as e2:
                return f"⚠️ Both models unavailable. Error: {e2}"
        return f"⚠️ Error: {e}"

# Streamlit UI
user_question = st.text_input("Enter your credit-related question:")
if st.button("Ask AI"):
    if user_question.strip():
        with st.spinner("Thinking..."):
            answer = generate_answer(user_question)
        st.success("✅ Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question first.")

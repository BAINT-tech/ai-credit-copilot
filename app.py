import streamlit as st
import google.generativeai as genai

# ---------------------------------
# 💳 AI Credit Copilot — Gemini Auto Edition
# ---------------------------------

st.set_page_config(page_title="💳 AI Credit Copilot", page_icon="💳")

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit with credit capilot AI.")

# 🔑 Load Google API Key
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", "")

if not GOOGLE_API_KEY:
    st.warning("⚠️ Please add your Google API key in Streamlit Secrets as 'GOOGLE_API_KEY'.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

    # ✅ Auto-detect available Gemini model
    try:
        available_models = [m.name for m in genai.list_models()]
        gemini_model = next((m for m in available_models if "gemini" in m.lower()), None)

        if gemini_model:
            model = genai.GenerativeModel(gemini_model)
            st.info(f"✅ Using model: **{gemini_model}**")
        else:
            st.error("⚠️ No Gemini model found. Check your API access or account permissions.")
            model = None
    except Exception as e:
        st.error(f"⚠️ Could not fetch model list: {str(e)}")
        model = None

# 🧠 User Input
credit_question = st.text_input("Enter your credit-related question:")

# 🚀 Run AI
if st.button("Ask Copilot"):
    if not GOOGLE_API_KEY:
        st.error("Missing API key. Add it in Streamlit Secrets.")
    elif not credit_question.strip():
        st.error("Please type a question before clicking 'Ask Copilot'.")
    elif model:
        with st.spinner("💭 Thinking..."):
            try:
                response = model.generate_content(credit_question)
                st.success("✅ Here's what I found:")
                st.write(response.text)
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
    else:
        st.error("No valid model available.")

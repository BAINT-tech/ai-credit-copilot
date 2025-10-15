import streamlit as st
import requests
import json

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit with Capilot AI.")

api_key = st.text_input("Enter your Gemini API Key:", type="password")

question = st.text_area("Enter your credit-related question:")

if st.button("Ask AI"):
    if not api_key or not question:
        st.warning("Please enter both your API key and a question.")
    else:
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{
                "parts": [{"text": f"Answer this credit-related question clearly and professionally: {question}"}]
            }]
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            try:
                text_output = result["candidates"][0]["content"]["parts"][0]["text"]
                st.success("✅ AI Credit Copilot says:")
                st.write(text_output)
            except Exception:
                st.error("⚠️ Unexpected response format from the API.")
                st.json(result)
        else:
            st.error(f"⚠️ Error {response.status_code}: {response.text}")

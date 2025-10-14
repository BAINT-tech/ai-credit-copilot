import streamlit as st
from openai import OpenAI

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit.")

# ✅ Correct client initialization
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input("Enter your credit-related question:")

if question:
    with st.spinner("Thinking..."):
        try:
            # ✅ Correct chat call for new OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an AI financial advisor that gives credit improvement tips."},
                    {"role": "user", "content": question},
                ]
            )
            st.success("✅ Here's your AI advice:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

import streamlit as st
from openai import OpenAI

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit.")

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input("Enter your credit-related question:")

if question:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI credit advisor."},
                {"role": "user", "content": question},
            ],
        )
        st.write(response.choices[0].message.content)

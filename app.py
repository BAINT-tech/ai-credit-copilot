import streamlit as st
from openai import OpenAI

# Initialize the client using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit.")

# User input
question = st.text_input("Enter your credit-related question:")

# When the button is clicked
if st.button("Ask Copilot"):
    if question:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful financial assistant that gives credit improvement advice."},
                {"role": "user", "content": question}
            ]
        )
        st.success(response.choices[0].message.content)
    else:
        st.warning("Please type a question first.")

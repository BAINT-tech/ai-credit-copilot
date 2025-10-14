import streamlit as st
import openai

# Load your OpenAI API key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit.")

# Input from user
question = st.text_input("Enter your credit-related question:")

# When the user clicks the button
if st.button("Ask Copilot"):
    if question:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a credit expert assistant helping users improve their financial health and credit score."},
                {"role": "user", "content": question}
            ]
        )
        st.success(response.choices[0].message.content)
    else:
        st.warning("Please type your question first.")

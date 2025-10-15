import streamlit as st
import random

st.set_page_config(page_title="💳 AI Credit Copilot", page_icon="💳")

st.title("💳 AI Credit Copilot")
st.write("Get AI-powered guidance to improve and manage your credit — now with dynamic answers!")

# Dynamic response generator
def get_dynamic_response(user_input):
    responses = {
        "credit score": [
            "Pay bills on time and keep your credit utilization under 30%.",
            "Dispute any errors on your credit report — even small ones matter.",
            "Increase your credit limit, but don’t use it fully — this improves utilization.",
            "Set up auto-pay to never miss a payment again.",
        ],
        "raise": [
            "Pay off high-interest debt first — it affects your score heavily.",
            "Avoid applying for too many new accounts in a short time.",
            "Make small purchases and pay them off early to show consistent usage.",
        ],
        "debt": [
            "Use the avalanche method to pay off high-interest debt faster.",
            "Avoid closing old credit cards — older accounts help your credit age.",
            "Negotiate lower interest rates to manage debt more easily.",
        ],
        "loan": [
            "Shop around before taking any loan — even a 1% rate difference saves hundreds.",
            "Make extra payments on your loan principal if you can.",
            "Avoid payday loans — they damage your credit quickly.",
        ],
        "report": [
            "Check your credit report from all three bureaus regularly.",
            "Look for fraudulent activity or duplicate accounts and report them immediately.",
            "Keep old accounts open — they show stability.",
        ],
    }

    matched_responses = []
    for keyword, possible_answers in responses.items():
        if keyword in user_input.lower():
            matched_responses.extend(possible_answers)

    if matched_responses:
        return random.choice(matched_responses)
    else:
        fallback = [
            "Keep consistent payments — lenders love reliability.",
            "Reduce your overall debt ratio over time for a stronger profile.",
            "Focus on stability: steady income, consistent payments, and low utilization.",
        ]
        return random.choice(fallback)

# User input section
user_question = st.text_input("Enter your credit-related question:")

if st.button("Get Advice"):
    if user_question.strip():
        answer = get_dynamic_response(user_question)
        st.success(f"✅ Answer:\n\n{answer}")
    else:
        st.warning("Please enter a question first.")

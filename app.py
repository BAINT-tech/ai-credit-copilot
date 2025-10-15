import streamlit as st

st.title("💳 AI Credit Copilot (Plan B)")
st.write("Test AI credit guidance instantly without API issues!")

# User input
question = st.text_area("Enter your credit-related question:")

if st.button("Ask AI"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        # Simulated AI response (replace with real API later)
        st.spinner("Thinking...")
        simulated_responses = {
            "credit score": "Focus on paying down debts, keeping balances low, and paying on time.",
            "debt": "Consider a debt snowball or avalanche method and avoid new high-interest loans.",
            "loan": "Check your interest rates and consolidate if needed for lower payments."
        }
        
        # Simple matching
        answer = next((v for k, v in simulated_responses.items() if k in question.lower()), 
                      "💡 Make sure to pay bills on time and monitor your credit regularly.")
        
        st.success("✅ AI Credit Copilot says:")
        st.write(answer)

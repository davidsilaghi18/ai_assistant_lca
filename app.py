import streamlit as st
import pandas as pd
from query_engine import ask_gpt

# Load dataset
df = pd.read_csv("buildings.csv")

# Streamlit page setup
st.set_page_config(page_title="LCA AI Assistant", layout="wide")
st.title("🧠 AI Assistant for Sustainability Data")
st.write("Ask a question about green buildings, CO2, energy, and more!")

# Show dataset in expandable section
with st.expander("📊 View Dataset"):
    st.dataframe(df)

# Input from user
question = st.text_input("Ask your question:")

# If user types a question
if question:
    st.write("🧾 You asked:", question)

    # Use first 5 rows of the dataset as context
    context = df.head().to_string(index=False)

    # Ask GPT
    response = ask_gpt(question, context)

    # Show response
    st.success(response)

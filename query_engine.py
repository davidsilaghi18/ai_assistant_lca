import openai
from config import OPENAI_API_KEY

# Set up the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to generate a response using GPT-3.5
def ask_gpt(question, context=""):
    prompt = f"""
You are an AI assistant that answers questions about sustainability, CO2, green buildings, and energy data.
Here is some context from the dataset:

{context}

User question: {question}

Provide a clear and helpful answer based only on the context.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # you can change to "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=200
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"❌ Error: {e}"

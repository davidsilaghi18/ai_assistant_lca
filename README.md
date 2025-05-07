# 🧠 AI Assistant for Sustainability Data

This project is a Streamlit-based web app that allows users to ask questions about sustainability data — such as green buildings, CO2, energy, and more — and get answers powered by GPT-3.5.

## 💡 Features

- View dataset of buildings (CSV file)
- Ask natural language questions about the data
- Uses OpenAI GPT API to generate answers based on dataset context
- .env file to keep your API key secure

## 🧪 Example Questions

- Which building has the highest carbon footprint?
- What is the average CO2 emissions?
- How many buildings use solar energy?

## ⚙️ Requirements

- Python 3.8+
- `openai`
- `pandas`
- `streamlit`
- `python-dotenv`

Install them with:

```bash
pip install -r requirements.txt


🚀 Run Locally
Clone the repo:

bash
Copiază
Editează
git clone https://github.com/davidsilaghi18/ai_assistant_lca.git
cd ai_assistant_lca
Create a .env file:

env
Copiază
Editează
OPENAI_API_KEY=your-key-here
Run the app:

bash
Copiază
Editează
streamlit run app.py
Open http://localhost:8501 in your browser.

🛡️ Note
This project does not include an API key. Users must create their own .env file with their OpenAI API key.

📄 License
This project is licensed under the MIT License. 

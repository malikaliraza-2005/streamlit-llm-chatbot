 🤖 Streamlit LLM Chatbot

📌 Description:

An interactive chatbot built using Streamlit and powered by the Llama 3.2 (1B) model via Ollama.
The application provides real-time conversational responses, maintains chat history using session state, and features a custom-styled user interface.

 🚀 Features:
 
* 💬 Real-time chat interface
* 🧠 Session-based memory (chat history persists during session)
* 🎨 Custom UI styling using CSS
* ⚡ Lightweight and fast performance
* 🔄 Interactive user–assistant conversation flow

 🛠️ Tech Stack:

* Python
* Streamlit
* Ollama
* Llama 3.2 (1B)

📂 Project Structure:

├── app.py
├── requirements.txt
├── style.css
└── README.md

⚙️ Installation:

1. Clone the repository:

git clone https://github.com/your-username/streamlit-llm-chatbot.git
cd streamlit-llm-chatbot

2. Install dependencies:
    
pip install -r requirements.txt

3. Install and run Ollama:

Make sure Ollama is installed and running locally:

ollama run llama3.2:1b

▶️ Usage:

Run the Streamlit app:

streamlit run app.py

Then open the browser and start chatting.

⚠️ Important Note:

This application uses Ollama to run the Llama 3.2 (1B) model locally.
It **will not work on cloud platforms** like Streamlit Cloud unless replaced with an API-based model.

🎯 How It Works:

1. User enters a message via chat input
2. Message is stored in Streamlit session state
3. Full conversation is sent to Ollama
4. Model generates a response
5. Response is displayed and stored in session

📜 License:

This project is licensed under the MIT License.

👤 Author:

Ali Raza

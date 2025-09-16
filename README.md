# Ai_Chatbot_Prototype
This project is an end-to-end AI chatbot built with Streamlit. It provides two implementations:  OpenAI GPT-based chatbot (app_openai.py)  Claude AI-based chatbot (app_claude.py) .Chat UI built with Streamlit  Supports both OpenAI GPT and Claude AI  Maintains conversation history  Easy deployment on Streamlit.

====================

This repository contains two end-to-end AI chatbot prototypes built using Streamlit and AI APIs (OpenAI & Claude).
You can run them locally or deploy them easily on Streamlit Cloud.

-------------------------------------------------------------

Files
-----
- app_openai.py  -> Chatbot powered by OpenAI GPT (gpt-3.5-turbo / gpt-4)
- app_claude.py  -> Chatbot powered by Claude AI (claude-3-sonnet / claude-3-haiku)

-------------------------------------------------------------

Setup & Installation
--------------------
1. Clone the repo:
   git clone https://github.com/your-username/ai-chatbot-prototype.git
   cd ai-chatbot-prototype

2. (Optional) Create a virtual environment:
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows

3. Install dependencies:
   pip install -r requirements.txt

-------------------------------------------------------------

Requirements
------------
Create a file called requirements.txt with the following:

streamlit
openai
anthropic

-------------------------------------------------------------

API Keys
--------
You need to set up your API keys before running:

For OpenAI:
    export OPENAI_API_KEY="your_openai_api_key"

For Claude:
    export ANTHROPIC_API_KEY="your_claude_api_key"

(On Windows PowerShell, use 'setx' instead of 'export').

-------------------------------------------------------------

Running the Apps
----------------
OpenAI Chatbot:
    streamlit run app_openai.py

Claude Chatbot:
    streamlit run app_claude.py

-------------------------------------------------------------

Deployment (Optional)
---------------------
You can deploy this repo for free on Streamlit Cloud:

1. Push this repo to GitHub
2. Log in to Streamlit Cloud and link your GitHub
3. Deploy either app_openai.py or app_claude.py
4. Share your public app link!

-------------------------------------------------------------

License
-------
MIT License - free to use and modify.

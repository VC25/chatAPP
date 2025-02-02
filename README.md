Streamlit Chatbot with OpenRouter API

This is a simple chatbot application built with Streamlit and OpenAI's OpenRouter API. It allows users to input their API key, interact with a chatbot using the meta-llama/llama-3.2-3b-instruct:free model, and receive AI-generated responses.

Features

Accepts user input through a chat interface

Uses OpenRouter API for generating AI responses

Stores chat history in session state

Secure API key input field

Streaming responses for a better user experience

Prerequisites

To run this application, you need:

Python 3.8+

A valid OpenRouter API key

Installation

Clone this repository:

git clone <repository-url>
cd <repository-folder>

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Usage

Run the Streamlit application:

streamlit run main.py

Enter your OpenRouter API key when prompted.

Start chatting with the AI!

Configuration

The chatbot uses the following default model:

meta-llama/llama-3.2-3b-instruct:free

You can modify the model by changing:

st.session_state["llm"] = "your-preferred-model"



💬 Gemini Chat Q&A Application

📘 Project Overview

This project is a conversational Q&A web application built using Streamlit and powered by Google's Gemini 1.5 Flash model. The application allows users to interact with the Gemini language model in a chat-like interface, maintaining context across multiple exchanges. It supports session-based conversation history, streaming responses, and secure input of the API key through the sidebar.

🔍 Key Features

->Natural language interaction with Gemini 1.5 Flash.

->Conversational memory with preserved chat history using session state.

->Streaming response generation for smoother UX.

->Lightweight, interactive UI built with Streamlit.

->Secure handling of the Google API key via the sidebar.

⚙️ How It Works

->The user enters their Google API key in the sidebar.

->A question is typed into the input box.

->Upon clicking "Ask the question", the app:

   o Initializes a Gemini chat session (if not already started),

   o Sends the question to the Gemini model,

   o Streams and displays the response in real-time,

   o Stores both question and answer in a chat history section.

->All interactions are retained until the session ends.

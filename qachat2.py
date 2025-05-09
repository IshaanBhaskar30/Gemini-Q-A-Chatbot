import streamlit as st
import google.generativeai as genai

# Streamlit page config
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Sidebar input for API Key
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'chat' not in st.session_state and api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    st.session_state['chat'] = model.start_chat(history=[])

# Input prompt and button
user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# Handle submission
if submit:
    if not api_key:
        st.error("Please enter your API key in the sidebar.")
    elif not user_input:
        st.warning("Please enter a question.")
    else:
        chat = st.session_state['chat']
        response = chat.send_message(user_input, stream=True)

        # Store user input
        st.session_state['chat_history'].append(("You", user_input))

        # Display and store streaming response
        st.subheader("The Response is")
        full_response = ""
        for chunk in response:
            st.write(chunk.text)
            full_response += chunk.text
        st.session_state['chat_history'].append(("Bot", full_response))

# Show chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

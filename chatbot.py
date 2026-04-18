import streamlit as st 
import ollama 

import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")


model = "llama3.2:1b" 
st.markdown("<h1 class='title'>Llama-3.2 VEX</h1>", unsafe_allow_html=True) 

if "messages" not in st.session_state:     
    st.session_state.messages = []    

for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message here...") 

if prompt:                                                                   
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)    
    response = ollama.chat(
        model=model,
        messages=st.session_state.messages,
        stream=False
    )
    assistant_message = response.message.content 
    st.session_state.messages.append({"role": "assistant", "content": assistant_message}) 

    with st.chat_message("assistant"): #Step 13: Displaying the assistant's message in the chat interface using the "assistant" role.
        st.write(assistant_message) 

#Flow of the code:
#1. The code starts by importing the necessary libraries: Streamlit for creating the web application interface and Ollama for interacting with the Ollama API to enable chatbot functionality.
#2. The model to be used for the chatbot is defined as "llama3.2:1b".   
#3. The title of the Streamlit application is set to "Chat with Ollama" using the st.title() function.
#4. The code checks if the "messages" key is not present in the Streamlit session state. If it's not present, it initializes it as an empty list. This allows the application to keep track of the conversation history between the user and the chatbot.
#5. The code iterates through the list of messages stored in the session state and displays each message in the chat interface. The role of the message (user or assistant) is used to determine how it should be displayed.
#6. A chat input field is created using st.chat_input() where the user can type their message.
#7. The code checks if the prompt variable contains any user input. If it does, the user's message is added to the session state messages list with the role "user".
#8. The user's message is displayed in the chat interface using the "user" role.
#9. The conversation history (stored in st.session_state.messages) is sent to the Ollama API using the chat method. The response from the API is stored in the response variable.
#10. The content of the assistant's message is extracted from the response and stored in the assistant_message variable.
#11. The assistant's message is added to the session state messages list with the role "assistant".
#12. The assistant's message is displayed in the chat interface using the "assistant" role.
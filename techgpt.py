from langchain_community.chat_models import ChatOpenAI  
from langchain.schema import SystemMessage, HumanMessage, AIMessage  
import streamlit as st
from streamlit_chat import message
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Streamlit page configuration
st.set_page_config(
    page_title="tecGPT",  
    page_icon="🤖"
)

# Display title
st.subheader("Custom GPT")

# Initialize ChatOpenAI model
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Sidebar for system and user input
with st.sidebar:  # Fixed typo `sitebar` to `sidebar`
    system_message = st.text_input(label="Assistant Role")
    user_prompt = st.text_input(label="Enter your prompt")

# Check and append messages
if system_message:
    # Add a system message if not already added
    if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
        st.session_state.messages.append(SystemMessage(content=system_message))

if user_prompt:
    # Add the user's message
    st.session_state.messages.append(HumanMessage(content=user_prompt))

    with st.spinner("Thinking..."):
        # Get response from the model
        response = chat(st.session_state.messages)
        # Append AI's response
        st.session_state.messages.append(AIMessage(content=response.content))

# Display messages
for i, msg in enumerate(st.session_state.messages[1:]):
    if i % 2 == 0:
        message(msg.content, is_user=True, key=f"{i}+ 😎")
    else:
        message(msg.content, is_user=False, key=f"{i}+ 😊")

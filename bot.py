import streamlit as st
import openai
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate  
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's queries."),
    ("user", "question: {question}")
])

# Define the response generation function
def generate_response(question, api_key, engine, temperature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=engine, temperature=temperature, max_tokens=max_tokens, openai_api_key=api_key)  # API key pass ki
    chain = LLMChain(prompt=prompt, llm=llm)
    answer = chain.run({'question': question})
    return answer

# Streamlit app
st.title("Enhanced Q&A Chatbot With OpenAI")

# Sidebar for settings
st.sidebar.title("Settings") 
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
engine = st.sidebar.selectbox("Select Open AI Model", ["gpt-3.5-turbo", "gpt-4", "gpt-4-0", "gpt-4-3"])
temperature = st.sidebar.slider('Temperature', min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=100, max_value=300, value=150)

# User input
st.write("Please ask your question")
user_input = st.text_input("Your prompt:")

if user_input and api_key:
    response = generate_response(user_input, api_key, engine, temperature, max_tokens)
    st.write(response)
elif user_input:
    st.warning("Please enter your OpenAI API Key in the sidebar.")
else:
    st.write("Please enter your question in the text box.")

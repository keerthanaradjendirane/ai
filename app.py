import google.generativeai as genai
import streamlit as st
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_content(prompt, max_words):
    # Include max_words in the prompt or use it as a parameter if supported
    response = model.generate_content([f"{prompt} (Max words: {max_words})"])
    return response.text

st.title("Generative AI Story Generator")
st.write("Select a genre and enter a prompt to generate content.")

genres = ["Comedy", "Horror", "Adventure", "Sci-Fi"]

selected_genre = st.selectbox("Choose a Genre", genres)
user_prompt = st.text_input("Enter your prompt")
max_words = st.slider("Select the number of words for the summary:", min_value=10, max_value=2000, value=100, step=10)

if st.button("Generate Content"):
    if user_prompt:
        content = generate_content(f"Generate a {selected_genre.lower()} story: {user_prompt}", max_words)
        st.write("Generated Content:")
        st.write(content)
    else:
        st.write("Please enter a prompt to generate content.")

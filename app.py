import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Helper function for question-answering
def get_answer(question, model="ft:gpt-4o-2024-08-06:personal:fic-lestari-bahasa-01:ANtvR3xr"):  # Use your fine-tuned model ID if available
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for answering questions in Indonesian languages."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content'].strip()

# Helper function for translation
def translate_text(text, target_language, model="ft:gpt-4o-2024-08-06:personal:fic-lestari-bahasa-01:ANtvR3xr"):  # Use your fine-tuned model ID if available
    prompt = f"Translate the following text to {target_language}: '{text}'"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful translator."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Streamlit UI setup
st.set_page_config(page_title="Ficky Language Assistant", layout="wide")
st.sidebar.title("Language Assistant")
page = st.sidebar.radio("Choose a function", ["Question Answering", "Translation"])

# Page for Question Answering
if page == "Question Answering":
    st.title("Question Answering Assistant")
    question = st.text_input("Ask a question:")
    if st.button("Get Answer"):
        if question:
            answer = get_answer(question)
            st.write("Answer:", answer)
        else:
            st.write("Please enter a question.")

# Page for Translation
elif page == "Translation":
    st.title("Translation Assistant")
    text = st.text_input("Enter text to translate:")
    target_language = st.selectbox("Select target language", ["Sundanese", "Javanese", "Balinese"])
    if st.button("Translate"):
        if text:
            translation = translate_text(text, target_language)
            st.write("Translation:", translation)
        else:
            st.write("Please enter text to translate.")

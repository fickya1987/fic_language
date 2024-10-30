import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Helper functions
def openai_completion(prompt, model="ft:gpt-4o-2024-08-06:personal:fic-lestari-bahasa-01:ANtvR3xr"):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=2000
    )
    return response.choices[0].text.strip()



# Page Configuration
st.set_page_config(page_title="Multi-Function Language Assistant", layout="wide")

# Sidebar navigation
st.sidebar.title("Language Assistant")
page = st.sidebar.radio("Choose a function", ["Question Answering", "Translation"])

# Page content based on selection
if page == "Question Answering":
    st.title("Question Answering")
    question = st.text_input("Ask a question:")
    if st.button("Get Answer"):
        if question:
            answer = openai_completion(question)
            st.write("Answer:", answer)

elif page == "Translation":
    st.title("Translation")
    sentence = st.text_input("Enter a sentence for translation:")
    target_language = st.selectbox("Select target language", ["Sundanese", "Javanese", "Balinese","buginese","ngaju"])
    if st.button("Translate"):
        if sentence:
            translation_prompt = f"Translate '{sentence}' to {target_language}."
            translation = openai_completion(translation_prompt)
            st.write("Translation:", translation)

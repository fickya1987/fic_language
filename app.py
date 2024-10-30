import os
import openai
import streamlit as st
from dotenv import load_dotenv
import pyttsx3
import speech_recognition as sr

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize TTS engine
engine = pyttsx3.init()

# Helper functions
def openai_completion(prompt, model="ft-your-model-id"):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError:
            return "Speech recognition service is unavailable"

# Page Configuration
st.set_page_config(page_title="Multi-Function Language Assistant", layout="wide")

# Sidebar navigation
st.sidebar.title("Language Assistant")
page = st.sidebar.radio("Choose a function", ["Question Answering", "Translation", "Text-to-Speech", "Speech-to-Text"])

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
    target_language = st.selectbox("Select target language", ["Sundanese", "Javanese", "Balinese"])
    if st.button("Translate"):
        if sentence:
            translation_prompt = f"Translate '{sentence}' to {target_language}."
            translation = openai_completion(translation_prompt)
            st.write("Translation:", translation)

elif page == "Text-to-Speech":
    st.title("Text-to-Speech")
    text = st.text_area("Enter text to convert to speech:")
    if st.button("Speak"):
        if text:
            text_to_speech(text)
            st.write("Speaking...")

elif page == "Speech-to-Text":
    st.title("Speech-to-Text")
    if st.button("Record and Convert"):
        result = speech_to_text()
        st.write("Converted Text:", result)

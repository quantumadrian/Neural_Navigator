import streamlit as st
from reader import extract_text_from_pdf
import requests
import json
import base64

# 🔑 Your Google Cloud API key (DO NOT share publicly)
API_KEY = "AIzaSyC2CWmn-UK9sGFpKBRjMYhJBqD10_RTyTo"

# TTS request via Google Cloud REST API
def speak_text_with_apikey(text, speed, pitch, api_key):
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={api_key}"

    headers = {"Content-Type": "application/json"}
    data = {
        "input": {"text": text},
        "voice": {
            "languageCode": "en-US",
            "name": "en-US-Studio-O"
        },
        "audioConfig": {
            "audioEncoding": "MP3",
            "speakingRate": speed,
            "pitch": pitch
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        audio_content = result["audioContent"]
        output_file = "tts_output.mp3"
        with open(output_file, "wb") as out:
            out.write(base64.b64decode(audio_content))
        return output_file
    else:
        st.error("🚨 TTS API Error:\n" + response.text)
        return None

# 🎛️ Streamlit App UI
st.set_page_config(page_title="🧠 ADHD TTS Assistant")
st.title("🗣️ ADHD Voice Assistant")

# Sidebar voice settings
st.sidebar.header("🎛️ Voice Settings")
speed = st.sidebar.slider("Speed", 0.25, 2.0, 1.0, step=0.05)
pitch = st.sidebar.slider("Pitch", -20.0, 20.0, 0.0, step=1.0)

# Section 1: Manual Text Input
st.subheader("✍️ Type Text to Speak")
typed_text = st.text_area("Enter text here:")

if st.button("🔊 Speak Typed Text"):
    if typed_text.strip():
        audio_path = speak_text_with_apikey(typed_text, speed, pitch, API_KEY)
        if audio_path:
            st.audio(audio_path, format="audio/mp3")
    else:
        st.warning("Please enter some text.")

st.markdown("---")

# Section 2: PDF Upload
st.subheader("📄 Upload a PDF to Read Aloud")
uploaded_pdf = st.file_uploader("Choose a PDF", type="pdf")

if uploaded_pdf and st.button("🔊 Speak PDF Text"):
    extracted_text = extract_text_from_pdf(uploaded_pdf)
    if extracted_text:
        audio_path = speak_text_with_apikey(extracted_text, speed, pitch, API_KEY)
        if audio_path:
            st.audio(audio_path, format="audio/mp3")
    else:
        st.warning("⚠️ No extractable text found in PDF.")


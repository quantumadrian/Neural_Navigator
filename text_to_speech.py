import streamlit as st
from reader import extract_text_from_pdf
from google.cloud import texttospeech


import os

def speak_text(text, speed, pitch):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Studio-O"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speed,
        pitch=pitch,
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config,
    )

    # Ensure 'static/' directory exists
    directory = "static/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, "tts_output.mp3")
    with open(filename, "wb") as out:
        out.write(response.audio_content)

    return filename

"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import re
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
# Instantiates a client

def txt2speech(project_name):
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    text_path = os.path.join('text', project_name + '.txt')
    with open(text_path, 'r', encoding='utf-8') as f:
        story_text = f.read()
    story_text = re.sub('\s', '', story_text)
    synthesis_input = texttospeech.types.SynthesisInput(text=story_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='cmn-TW',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    audio_path = os.path.join('output_project', project_name, 'voice')
    # The response's audio_content is binary.
    if not os.path.exists(audio_path):
        os.makedirs(audio_path)
    with open(os.path.join(audio_path, "{}.mp3".format(project_name)), 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
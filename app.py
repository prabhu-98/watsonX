import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import streamlit as st

# Replace 'your-api-key' and 'your-service-url' with your actual credentials
api_key = '_2bq6TI28ocEg7FYGwwSUaNE-5w7LiPasT6ilklbilgj'
service_url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/6f2af861-894a-4c64-9e52-9a8ca06f6b42'

# Set up the Speech to Text service
authenticator = IAMAuthenticator(api_key)
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url(service_url)

# Function to transcribe audio
def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        result = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav'
        ).get_result()
        
    return result

# Example usage
if __name__ == "__main__":
    audio_file_path = r'C:\Users\PRABHU DAS\Desktop\watsonx\harvard.wav'
    transcript = transcribe_audio(audio_file_path)
    print(json.dumps(transcript, indent=2))
st.wri



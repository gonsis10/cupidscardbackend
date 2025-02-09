from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import subprocess

def get_title_length(file_path):
    """Get audio duration using ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", 
         "format=duration", "-of", 
         "default=noprint_wrappers=1:nokey=1", file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

def transcribe_audio_to_text():
    authenticator = IAMAuthenticator('pyLdoDRm-_fxr9OrRgwLr_ZvBZoglpReBEnTd3tuUwFn')
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )
    speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/36d439b8-5a01-49ab-984b-724ee587499a')
    
    title_length = get_title_length("./temp/title_sped.mp3")

    with open("./temp/content_sped.mp3", "rb") as audio_file:
        response = speech_to_text.recognize(
            audio=audio_file,
            content_type="audio/mp3",
            timestamps=True,  # Request timestamps for each word
            word_alternatives_threshold=0.9  # Optional: Adjust to get word alternatives
        ).get_result()

    words = []
    # Print the word-by-word transcription with timestamps
    for result in response["results"]:
        for alternative in result["alternatives"]:
            for word, start_time, end_time in alternative["timestamps"]:
                words.append({"text": word, "start": round(start_time + title_length, 2), "end": round(end_time + title_length, 2)})

    return words, title_length

# with open('./temp/words_transcriber.json', 'w') as json_file:
#     json.dump(transcribe_audio_to_text(), json_file)
    
# print("done")
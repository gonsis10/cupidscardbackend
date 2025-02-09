import os
from video_setup import setup_background
from crop import crop_video
from video_composer import compose_video
from reddit import choose_post
from audio import create_audio
from edit_image import create_intro
from transcriber import transcribe_audio_to_text

def create_video():
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    # status, title, content = choose_post() # CHANGE THIS TO JSON FILE
    greeting = "Temp Title"
    content = "What if you could play Cupid for a day and help random strangers find love? In this video, the host (you) goes around asking people if they want a personalized Valentine's Day match based on random/funny questions."
    
    if True:
        print("1: Selected post, now creating audios")
        # create_audio(greeting, content)
        print("2: Created audios, now creating intro")
        # create_intro(greeting) # MIGHT NOT BE NECESSARY
        print("3: Created intro, now transcribing audios into word list and calculating intro length")
        words, intro_length = transcribe_audio_to_text() # TRANSCRIBE AUDIO TO WORD LIST
        print("4: Transcribed audios into word list and calculating intro length, now setting up background video")
        print("5: Setup background video, now composing short video")
        compose_video(words, intro_length)
        print("6: Finished composing final video")

if __name__ == "__main__":
    create_video()
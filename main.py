from video_setup import setup_background
from crop import crop_video
from video_composer import compose_video
from reddit import choose_post
from audio import create_audio
from edit_image import create_intro
from transcriber import transcribe_audio_to_text

def create_video():
    status, title, content = choose_post() # CHANGE THIS TO JSON FILE
    if status:
        print("1: Selected post, now creating audios")
        create_audio(title, content) # CHANGE A LITTLE BIT AUDIO
        print("2: Created audios, now creating intro")
        create_intro(title) # MIGHT NOT BE NECESSARY
        print("3: Created intro, now transcribing audios into word list and calculating intro length")
        words, intro_length = transcribe_audio_to_text() # TRANSCRIBE AUDIO TO WORD LIST
        print("4: Transcribed audios into word list and calculating intro length, now setting up background video")
        print("5: Setup background video, now composing short video")
        compose_video(words, intro_length)
        print("6: Finished composing final video")

if __name__ == "__main__":
    create_video()
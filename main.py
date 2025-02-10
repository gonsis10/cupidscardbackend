import os
import sys
from video_composer import compose_video
from audio import create_audio
from transcriber import transcribe_audio_to_text
import boto3

def create_video(full_message):
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    # status, title, content = choose_post() # CHANGE THIS TO JSON FILE
    greeting = "Cupids Card!"
    # content = "What if you could play Cupid for a day and help random strangers find love? In this video, the host (you) goes around asking people if they want a personalized Valentine's Day match based on random/funny questions."
    
    print("1: Selected post, now creating audios")
    create_audio(greeting, full_message)
    print("2: Created audios, now creating intro")
    # create_intro(greeting) # MIGHT NOT BE NECESSARY
    print("3: Created intro, now transcribing audios into word list and calculating intro length")
    words, intro_length = transcribe_audio_to_text() # TRANSCRIBE AUDIO TO WORD LIST
    print("4: Transcribed audios into word list and calculating intro length, now setting up background video")
    print("5: Setup background video, now composing short video")
    compose_video(words, intro_length)
    print("6: Finished composing final video")
        

def upload_video(video_id):
    s3 = boto3.client("s3")
    BUCKET_NAME = "cupidscard"

    # Upload File to S3 with Unique Name
    s3.upload_file("output/final_video.mp4", BUCKET_NAME, video_id)

    # Generate direct public URLfile_url
    file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{video_id}"
    print("✅ Public URL:", file_url)

    return file_url


def clean_up():
    greet_file = "audio/greeting.mp3"
    content_file = "audio/content.mp3"
    output_file = "output/final_video.mp4"
    
    if os.path.exists(greet_file):
        os.remove(greet_file)
    if os.path.exists(content_file):
        os.remove(content_file)
    if os.path.exists(output_file):
        os.remove(output_file)
    
    print("Cleaned up temporary files!")
    


if __name__ == "__main__":
    full_message = sys.argv[1]  # First argument: message
    video_id = sys.argv[2]   # Second argument: output file name
    
    create_video(full_message)
    upload_video(video_id)
    clean_up()

import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip
import os
os.environ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/magick"
from textwrap import fill
import pysrt
import numpy as np
from PIL import Image
from video_setup import setup_background
import json
    
def create_text_clip(txt, start_time, end_time, fontsize=60, pos=('center', 'center')):
    # wrapped_text = fill(txt, width=80)
    # text_clip = mp.TextClip(wrapped_text, fontsize=fontsize, color='white', font="Arial-Bold")
    # animated_clip = text_clip.set_start(start_time).set_duration(end_time - start_time).set_position(pos)
    
    wrapped_text = fill(txt, width=80)
    text_clip_outline = mp.TextClip(wrapped_text, fontsize=fontsize, color="black", font="Arial-Bold", stroke_color="black", stroke_width=2)
    text_clip = mp.TextClip(wrapped_text, fontsize=fontsize, color='white', font="Arial-Bold")
    composite_clip = mp.CompositeVideoClip([text_clip_outline, text_clip])
    return composite_clip.set_start(start_time).set_duration(max(0, end_time - start_time)).set_position(pos)

def add_subtitles(words, intro_length, video_clip):
    # Dummy parsing function - replace with actual parsing of your SRT file
    # subtitles = parse_srt(srt_path)
    # subtitles = transcribe_audio_to_text()
    # try:
    #     with open('./temp/words_transcriber.json', 'r') as json_file:
    #         subtitles = json.load(json_file)
    #     print("FOUND FILE")
    # except Exception as e:
    #     print(f"Failed to load subtitles: {e}")
    #     return video_clip
    subtitles = words
    
    clips = [video_clip]
    
    image_clip = mp.ImageClip("./temp/title_page.png").set_start(0).set_duration(intro_length)
    image_clip = image_clip.set_pos('center')
    image_clip = image_clip.resize(video_clip.size)
    clips.append(image_clip)
    
    
    for subtitle in subtitles:
        animated_text_clip = create_text_clip(
            subtitle["text"], 
            subtitle["start"], 
            subtitle["end"]
        )
        clips.append(animated_text_clip)

    # Combine original video with all animated text clips
    final_clip = mp.CompositeVideoClip(clips)
    
    return final_clip


# Run the functions
def compose_video(words, intro_length):
    input_clip = setup_background()

    # Add animated subtitles
    final_video = add_subtitles(words, intro_length, input_clip)
    final_video = final_video.fadein(1)
    # Write the result to a file
    final_video.write_videofile("./output/final_video.mp4", codec="mpeg4", threads=12, bitrate="8000k")

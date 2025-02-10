import moviepy.editor as mp
import os
os.environ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/magick"
from textwrap import fill
from video_setup import setup_background

def create_text_clip(txt, start_time, end_time, fontsize=60, pos=('center', 'center')):
    wrapped_text = fill(txt, width=80)
    text_clip_outline = mp.TextClip(wrapped_text, fontsize=fontsize, color="black", font="Arial-Bold", stroke_color="black", stroke_width=2, method="caption")
    text_clip = mp.TextClip(wrapped_text, fontsize=fontsize, color='white', font="Arial-Bold", method="caption")
    composite_clip = mp.CompositeVideoClip([text_clip_outline, text_clip])
    return composite_clip.set_start(start_time).set_duration(max(0, end_time - start_time)).set_position(pos)

def add_subtitles(words, intro_length, video_clip):
    subtitles = words
    
    clips = [video_clip]
    
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
    # print(input_clip.audio)

    # Add animated subtitles
    final_video = add_subtitles(words, intro_length, input_clip)
    final_video = final_video.fadein(1)
    # Write the result to a file
    final_video.write_videofile(
        "output/final_video.mp4",
        codec="libx264",  # Use libx264 for better compatibility
        audio_codec="aac",  # Ensure audio is encoded properly
        threads=12,
        bitrate="6000k"
    )


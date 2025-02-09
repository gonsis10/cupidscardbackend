import moviepy.editor as mp
import random

def setup_background():
    input_clip = mp.VideoFileClip("./assets/scene2.mp4")
    title_audio_clip = mp.AudioFileClip("./temp/title_sped.mp3")
    content_audio_clip = mp.AudioFileClip("./temp/content_sped.mp3")
    mixed_audio_clip = mp.CompositeAudioClip([mp.concatenate_audioclips([title_audio_clip, content_audio_clip]), mp.AudioFileClip("./assets/intro.mp3")])
    
    max_start = input_clip.duration - mixed_audio_clip.duration
    random_start = random.uniform(0, max_start)
    
    random_video_segment = input_clip.subclip(random_start, random_start + mixed_audio_clip.duration)

    final_clip = random_video_segment.set_audio(mixed_audio_clip)
    final_clip = final_clip.subclip(0, mixed_audio_clip.duration)
    return final_clip


# setup_background()
from elevenlabs import play, Voice, VoiceSettings, save
from elevenlabs.client import ElevenLabs
import subprocess

def speed_up_audio(input_file, output_file, speed_factor):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-filter:a', f'atempo={speed_factor}',
        '-vn',
        output_file
    ]
    subprocess.run(command)

def create_audio(title, content):
    client = ElevenLabs(
    api_key="68412013921e765bd947ba2d5b6b69a5", # Defaults to ELEVEN_API_KEY
    )

    bob = Voice(
                voice_id = "ZQe5CZNOzWyzPSCn5a3c",
            settings = VoiceSettings(
                stability = 0.5,
                similarity_boost = 0.60,
            )
        )

    title_audio = client.generate(
        text = title.replace("AITA", "Am I the asshole").replace("AMITA", "Am I the asshole").replace("WIBTA", "Am I the asshole"),
        voice = bob
    )

    content_audio = client.generate(
        text = content.replace("AITA", "Am I the asshole").replace("AMITA", "Am I the asshole").replace("WIBTA", "Am I the asshole"),
        voice = bob
    )
    
    # play(audio)
    save(title_audio, "./temp/title.mp3")
    save(content_audio, "./temp/content.mp3")
    
    # Usage example
    speed_up_audio('./temp/title.mp3', './temp/title_sped.mp3', 1.35)
    speed_up_audio('./temp/content.mp3', './temp/content_sped.mp3', 1.35)
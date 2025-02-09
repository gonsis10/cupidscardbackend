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

def create_audio(greeting, content):
    client = ElevenLabs(
    api_key="sk_32334211b2bfce0b57fc583832a6cdeadb0a3180cbdb79fe", # Defaults to ELEVEN_API_KEY
    )

    bob = Voice(
                voice_id = "ZQe5CZNOzWyzPSCn5a3c",
            settings = VoiceSettings(
                stability = 0.5,
                similarity_boost = 0.60,
            )
        )

    greeting_audio = client.generate(
        text = greeting,
        voice = bob
    )

    content_audio = client.generate(
        text = content,
        voice = bob
    )
    
    # play(audio)
    save(greeting_audio, "audio/greeting.mp3")
    save(content_audio, "audio/content.mp3")
    
    # Usage example
    # speed_up_audio('./temp/title.mp3', './temp/title_sped.mp3', 1.35)
    # speed_up_audio('./temp/content.mp3', './temp/content_sped.mp3', 1.35)
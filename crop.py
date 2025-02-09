import subprocess

def crop_video():
    input_file = './assets/scene3.mp4'
    output_file = './temp/scene3.mp4'
    # FFmpeg command components
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_file,  # Input file
        '-vf', 'crop=ih*9/16:ih:(iw-ow)/2:0',  # Video filter for cropping
        '-c:a', 'copy',  # Copy audio without re-encoding
        output_file  # Output file
    ]
    
    # Execute the FFmpeg command
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Video successfully cropped to 9:16 aspect ratio: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error cropping video: {e}")
        
# crop_video()
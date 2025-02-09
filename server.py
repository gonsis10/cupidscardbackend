from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import uuid
import os

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Directory to store generated videos
VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

@app.route("/generate_video", methods=["POST"])
def generate_video():
    data = request.get_json()
    message = data.get("message", "")
    recipient = data.get("recipient", "")
    sender = data.get("sender", "")

    # Create a unique video filename
    video_id = str(uuid.uuid4()) + ".mp4"
    output_file = os.path.join(VIDEO_DIR, video_id)

    # Call your existing Python script (modify this to match your script's format)
    subprocess.run(["python", "main.py", message, output_file])

    # Check if video was created
    if os.path.exists(output_file):
        return jsonify({"video_url": f"http://your-server.com/videos/{video_id}"})
    else:
        return jsonify({"error": "Video generation failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)

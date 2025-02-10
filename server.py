from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import subprocess
import uuid
import os

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

@app.route("/generate_video", methods=["POST"])
def generate_video():
    BUCKET_NAME = "cupidscard"
    data = request.get_json()

    # Extract message, recipient, and sender safely
    recipient = data.get("recipient", "Unknown Recipient")
    sender = data.get("sender", "Anonymous")
    message = data.get("message", "")

    # Format the full message
    full_message = f"Dear: {recipient}\n\n{message}\n\nLove: {sender}"

    # Create a unique video filename
    video_id = str(uuid.uuid4()) + ".mp4"

    # Run video generation asynchronously using `subprocess.Popen`
    try:  
        python_executable = sys.executable 
        process = subprocess.Popen([python_executable, "main.py", full_message, video_id])
    except Exception as e:
        return jsonify({"error": f"Video generation failed: {str(e)}"}), 500

    # Respond immediately while the video is being processed
    return jsonify({
        "message": "Video generation started",
        "video_id": video_id,
        "video_url": f"https://{BUCKET_NAME}.s3.amazonaws.com/{video_id}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

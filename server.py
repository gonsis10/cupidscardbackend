from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import sys
import subprocess
import uuid

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend
socketio = SocketIO(app, cors_allowed_origins="*")  # Enable WebSocket events

BUCKET_NAME = "cupidscard"

@app.route("/generate_video", methods=["POST"])
def generate_video():
    data = request.get_json()

    # Extract message, recipient, and sender safely
    recipient = data.get("recipient", "Unknown Recipient")
    sender = data.get("sender", "Anonymous")
    message = data.get("message", "")

    # Format the full message
    full_message = f"Dear: {recipient}\n\n{message}\n\nLove: {sender}"

    # Create a unique video filename
    video_id = str(uuid.uuid4()) + ".mp4"

    # Get the Socket.IO client ID from the request headers
    client_id = request.headers.get("Socket-ID")
    if not client_id:
        return jsonify({"error": "Socket-ID is required"}), 400

    # Start video generation using subprocess.Popen
    process = subprocess.Popen([sys.executable, "main.py", full_message, video_id])

    # Start a background task to notify when done
    socketio.start_background_task(wait_for_completion, process, video_id, client_id)

    # Respond immediately while the video is being processed
    return jsonify({
        "message": "Video generation started",
        "video_id": video_id,
        "video_url": f"https://{BUCKET_NAME}.s3.amazonaws.com/{video_id}"
    })

def wait_for_completion(process, video_id, client_id):
    """Wait for the subprocess to complete and notify the client."""
    process.wait()  # Wait for the process to finish

    # Notify the frontend when the video is done
    socketio.emit("video_ready", {"video_id": video_id, "video_url": f"https://{BUCKET_NAME}.s3.amazonaws.com/{video_id}"}, room=client_id)

@socketio.on("connect")
def handle_connect():
    print("Client connected:", request.sid)

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected:", request.sid)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)

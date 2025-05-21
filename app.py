from flask import Flask, request, jsonify, send_file, send_from_directory
import os
from reverse_video import reverse_video  # Ensure this function exists

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

# Create necessary folders
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')  # Ensure static/index.html exists

@app.route('/process-video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    video_file = request.files['video']

    # Use fixed filename
    input_filename = "sample.mp4"
    output_filename = "reversed_sample.mp4"

    input_path = os.path.join(UPLOAD_FOLDER, input_filename)
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    try:
        video_file.save(input_path)
    except Exception as e:
        return jsonify({"error": f"Failed to save video: {str(e)}"}), 500

    try:
        reverse_video(input_path, output_path)
    except Exception as e:
        return jsonify({"error": f"Processing error: {str(e)}"}), 500

    try:
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": f"Failed to send file: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

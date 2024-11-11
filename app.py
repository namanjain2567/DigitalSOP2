import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS



app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


# Path to the public SOP folder (shared network folder)
SOP_FOLDER_PATH = r'C:\Users\naman\SOP'
 # Use the actual path of your shared folder

# Endpoint to list SOP files (JSON, MP4)
@app.route('/sop/files', methods=['GET'])
def list_files():
    files = [f for f in os.listdir(SOP_FOLDER_PATH) if f.endswith(('.json', '.mp4'))]
    return jsonify(files), 200

# Endpoint to get the content of a specific SOP file (JSON or MP4)
@app.route('/sop/<filename>', methods=['GET'])
def get_sop_file(filename):
    file_path = os.path.join(SOP_FOLDER_PATH, filename)
    if os.path.exists(file_path):
        if filename.endswith('.json'):
            with open(file_path, 'r') as file:
                content = file.read()
            return content, 200
        elif filename.endswith('.mp4'):
            return send_from_directory(SOP_FOLDER_PATH, filename), 200
    else:
        return 'File not found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Accessible on the network

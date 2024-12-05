from flask import Flask, jsonify, send_from_directory, abort
import os

app = Flask(__name__)

# Define the base directories for the image folders
IMAGE_FOLDERS = {
    'face_swap': 'face_swap/model_img',
    'img': 'img',
    'img_style': 'img_style',
    'main_explore': 'main_explore'
}

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "success", "message": "pong"})

@app.route('/config', methods=['GET'])
def get_config():
    try:
        with open('config.json', 'r') as file:
            config_data = json.load(file)  # Load the JSON data from the file
        return jsonify(config_data)  # Return the data as JSON
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "config.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON format in config.json"}), 400

@app.route('/explore', methods=['GET'])
def get_explore():
    try:
        with open('explore.json', 'r') as file:
            explore_data = json.load(file)  # Load the JSON data from the file
        return jsonify(explore_data)  # Return the data as JSON
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "explore.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON format in explore.json"}), 400

@app.route('/inspiration', methods=['GET'])
def get_inspiration():
    try:
        with open('inspiration.json', 'r') as file:
            inspiration_data = json.load(file)  # Load the JSON data from the file
        return jsonify(inspiration_data)  # Return the data as JSON
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "inspiration.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON format in inspiration.json"}), 400

@app.route('/main_explore', methods=['GET'])
def get_main_explore():
    try:
        with open('main_explore.json', 'r') as file:
            inspiration_data = json.load(file)  # Load the JSON data from the file
        return jsonify(inspiration_data)  # Return the data as JSON
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "main_explore.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON format in main_explore.json"}), 400

@app.route('/native_ad', methods=['GET'])
def get_native_ad():
    try:
        with open('native_ad.json', 'r') as file:
            inspiration_data = json.load(file)  # Load the JSON data from the file
        return jsonify(inspiration_data)  # Return the data as JSON
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "native_ad.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON format in native_ad.json"}), 400

@app.route('/style', methods=['GET'])
def get_style():
    try:
        with open('style.json', 'r') as file:
            inspiration_data = json.load(file)  # Load the JSON data from the file
        return jsonify(inspiration_data)  # Return the data as JSON
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "style.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON format in style.json"}), 400

@app.route('/face_swap_model', methods=['GET'])
def get_face_swap_model():
    try:
        with open('face_swap_model.json', 'r') as file:
            inspiration_data = json.load(file)  # Load the JSON data from the file
        return jsonify(inspiration_data)  # Return the data as JSON
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "face_swap_model.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON format in face_swap_model.json"}), 400


# New route to serve images from the specified directories
@app.route('/images/<folder>/<filename>', methods=['GET'])
def serve_image(folder, filename):
    # Ensure the folder is one of the allowed folders
    if folder not in IMAGE_FOLDERS:
        return jsonify({"status": "error", "message": f"Folder '{folder}' not allowed"}), 400

    # Get the directory path for the requested folder
    folder_path = IMAGE_FOLDERS[folder]

    # Check if the file exists in the specified folder
    file_path = os.path.join(folder_path, filename)
    if not os.path.exists(file_path):
        return jsonify({"status": "error", "message": f"File '{filename}' not found in '{folder}' folder"}), 404

    # Serve the image file from the specified folder
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

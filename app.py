from flask import Flask, jsonify
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
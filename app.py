from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "success", "message": "pong"})

@app.route('/config', methods=['GET'])
def get_config():
    # Path to your config.json file
    try:
        with open('config.json', 'r') as file:
            config_data = json.load(file)  # Load the JSON data from the file
        return jsonify(config_data)  # Return the data as JSON
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "config.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Invalid JSON format in config.json"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

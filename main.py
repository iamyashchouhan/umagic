from flask import Flask, request, jsonify
from gradio_client import Client

# Initialize Flask app
app = Flask(__name__)

# Gradio Client setup
client = Client("lelafav502/txt2txt")

@app.route('/ai/art/txt2img/', methods=['POST'])
def process_data():
    # Get JSON data from the request
    data = request.get_json()

    # Print all the values in the JSON request
    print("Received data:", data)

    # Extract values from the incoming request
    prompt = data.get('prompt', '')
    ratio = data.get('ratio', '')
    style = data.get('style', '')
    uuid_value = data.get('uuid_value', '')
    token = data.get('token', '')

    # Optionally, you can pass these to the Gradio client and print the result
    result = client.predict(
        prompt=prompt,
        ratio=ratio,
        style=style,
        uuid_value=uuid_value,
        token=token,
        api_name="/send_text2image_request"
    )

    # Print the result from the Gradio client
    print("Gradio client result:", result)

    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    # Bind the app to all network interfaces (0.0.0.0) and specify the port (e.g., 5000)
    app.run(host='0.0.0.0', port=5000, debug=True)

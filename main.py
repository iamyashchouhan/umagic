from flask import Flask, request, jsonify
from gradio_client import Client
import json  # To decode string responses into dictionaries if needed

# Initialize Flask app
app = Flask(__name__)

# Gradio Client setup for txt2txt (text-to-image model)
txt2img_client = Client("lelafav502/txt2txt")

# Gradio Client setup for img2img (image-to-image model)
img2img_client = Client("lelafav502/txt2txt") 

inpaint_client = Client("lelafav502/txt2txt") 

@app.route('/ai/art/txt2img/', methods=['POST'])
def process_txt2img_data():
    # Get form data from the request
    is_translate = request.form.get('is_translate', '')
    is_first = request.form.get('is_first', '')
    style_id = request.form.get('style_id', '')
    prompt = request.form.get('prompt', '')
    ratio = request.form.get('ratio', '')
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')

    # You can print the received form data
    print("Received form data:")
    print(f"is_translate: {is_translate}, is_first: {is_first}, style_id: {style_id}, prompt: {prompt}, ratio: {ratio}")

    # Check for required parameters
    if not prompt or not ratio:
        return jsonify({"error": "Missing required parameters: 'prompt' or 'ratio'"}), 400

    # Call Gradio client for txt2img
    result = txt2img_client.predict(
        prompt=prompt,
        ratio=ratio,
        style=style_id,  # Use style_id from the form data
        uuid_value=uuid_value,
        token=token,
        api_name="/send_text2image_request"
    )

    # Print the result from the Gradio client
    print("Gradio client result:", result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print("Parsed result from Gradio:", result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/img2img/', methods=['POST'])
def process_img2img_data():
    # Get form data from the request
    is_translate = request.form.get('is_translate', '')
    is_first = request.form.get('is_first', '')
    style_id = request.form.get('style_id', '')
    ratio = request.form.get('ratio', '')
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    image = request.form.get('image_name')  # Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"is_translate: {is_translate}, is_first: {is_first}, style_id: {style_id}, ratio: {ratio}")

    # Check for required parameters
    if not ratio or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)
    

    # Call Gradio client for img2img
    result = img2img_client.predict(
        image=image,  # Path to the uploaded image
        ratio=ratio,
        style=style_id,  # Use style_id from the form data
        uuid_value=uuid_value,
        token=token,
        api_name="/send_image2image_request"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/lineart/', methods=['POST'])
def process_doodle_data():
    # Get form data from the request
    is_translate = request.form.get('is_translate', '')
    is_first = request.form.get('is_first', '')
    style_id = request.form.get('style_id', '')
    ratio = request.form.get('ratio', '')
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    image = request.form.get('image_name')  # Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"is_translate: {is_translate}, is_first: {is_first}, style_id: {style_id}, ratio: {ratio}")

    # Check for required parameters
    if not ratio or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = img2img_client.predict(
        image=image,  # Path to the uploaded image
        ratio=ratio,
        style=style_id,  # Use style_id from the form data
        uuid_value=uuid_value,
        token=token,
        api_name="/send_image2image_request"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/inpaint/', methods=['POST'])
def process_inpaint_data():
    # Get form data from the request
    is_translate = request.form.get('is_translate', '')
    is_first = request.form.get('is_first', '')
    style_id = request.form.get('style_id', '')
    ratio = request.form.get('ratio', '')
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    prompt = request.form.get('prompt', '')
    mask = request.form.get('mask_name')
    image = request.form.get('image_name')  # Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"is_translate: {is_translate}, is_first: {is_first}, style_id: {style_id}, ratio: {ratio}")

    # Check for required parameters
    if not ratio or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = inpaint_client.predict(
        image=image, 
        mask=mask,
        ratio=ratio,
        uuid_value=uuid_value,
        token=token,
        prompt=prompt,
        style="0",
        api_name="/send_inpaint2image_request"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

if __name__ == '__main__':
    # Bind the app to all network interfaces (0.0.0.0) and specify the port (e.g., 5000)
    app.run(host='0.0.0.0', port=3000, debug=True)

import gradio as gr
from gradio_client import Client

# Initialize the Gradio Client API
client = Client("flux-ai/216.48.185.71")

# Define the function that will be triggered by the Gradio interface
def send_request(prompt, ratio, style, uuid_value, token):
    # Call the Gradio Client API
    result = client.predict(
        prompt=prompt,
        ratio=ratio,
        style=style,
        uuid_value=uuid_value,
        token=token,
        api_name="/send_text2image_request"
    )
    return result

# Create the Gradio interface
iface = gr.Interface(
    fn=send_request,  # Function to call when the user submits the form
    inputs=[
        gr.Textbox(label="Prompt"),       # Textbox for the 'prompt' input
        gr.Textbox(label="Ratio"),        # Textbox for the 'ratio' input
        gr.Textbox(label="Style"),        # Textbox for the 'style' input
        gr.Textbox(label="UUID Value"),   # Textbox for the 'uuid_value' input
        gr.Textbox(label="Token")         # Textbox for the 'token' input
    ],
    outputs="text",  # Display the result in text format
    live=False  # You can set this to True if you want real-time prediction as the user types
)

# Launch the interface
iface.launch()

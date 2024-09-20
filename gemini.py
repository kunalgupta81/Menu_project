from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key
genai.configure(api_key="AIzaSyD_NP9TmFcYRtxwkc7SGfQsqHO3S-IX6mc")

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

@app.route('/')
def index():
    return render_template("gemini.html")

@app.route('/generate-text', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return "No prompt provided.", 400

    try:
        # Start a chat session
        chat_session = model.start_chat(history=[])
        # Send the prompt to the model and get the response
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)

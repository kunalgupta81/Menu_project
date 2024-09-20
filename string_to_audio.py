from flask import Flask, request, send_file, render_template
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('string_to_audio.html')

@app.route('/stringtoaudio', methods=['POST'])
def string_to_audio():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return "Text is required", 400

    tts = gTTS(text)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    return send_file(audio_file, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

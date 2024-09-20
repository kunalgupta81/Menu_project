from flask import Flask, request, jsonify, render_template
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('click_photo.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.get_json()
    image_data = data.get('image')
    
    if image_data:
        # Remove the data URL scheme (e.g., "data:image/png;base64,")
        image_data = image_data.split(',')[1]
        
        # Decode the base64 string to binary data
        image_binary = base64.b64decode(image_data)
        
        # Open the image with PIL
        image = Image.open(BytesIO(image_binary))
        
        # Save the image
        image.save('captured_photo.png')
        
        return jsonify({'status': 'success', 'message': 'Image saved successfully!'})
    else:
        return jsonify({'status': 'error', 'message': 'No image data received'}), 400

if __name__ == '__main__':
    app.run(debug=True)

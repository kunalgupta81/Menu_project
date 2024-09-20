from flask import Flask, jsonify, request, send_file, render_template
import cv2
import numpy as np
import io
from PIL import Image

app = Flask(__name__)

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.route('/')
def index():
    return render_template('face_detection.html')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        # Initialize the camera
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            raise Exception("Could not open video device")

        # Capture a frame
        ret, frame = cap.read()
        cap.release()

        if not ret:
            raise Exception("Could not read frame from video device")

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Convert the frame with detected faces to PIL Image
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)

        # Save the image to a BytesIO object
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        return send_file(img_bytes, mimetype='image/png', as_attachment=False)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=80)

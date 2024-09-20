from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def index():
    return render_template('get cordinates.html')

# Route to handle coordinates and place data
@app.route('/save_coordinates', methods=['POST'])
def save_coordinates():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    place = data.get('place')

    # Print the received data (for demonstration purposes)
    print(f"Latitude: {latitude}, Longitude: {longitude}, Place: {place}")

    # Respond back to the client
    return jsonify({'status': 'success', 'message': 'Coordinates and place saved'}), 200

if __name__ == '__main__':
    app.run(debug=True)

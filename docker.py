from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Placeholder function to simulate Docker metrics fetching
def get_docker_metrics():
    # Replace with actual Docker API call if available
    metrics = {
        'memory': [random.randint(40, 100) for _ in range(5)],  # Simulate memory usage data
        'status': ['Running' if random.choice([True, False]) else 'Stopped' for _ in range(5)],  # Simulate status data
        'storage': [random.randint(10, 50) for _ in range(5)]  # Simulate storage usage data
    }
    return metrics

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('docker_dashboard.html')

# API route to get Docker metrics
@app.route('/metrics', methods=['GET'])
def get_metrics():
    metrics = get_docker_metrics()
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)

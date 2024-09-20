from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def live_camera():
    return render_template('live_camera.html')

if __name__ == '__main__':
    app.run(debug=True)

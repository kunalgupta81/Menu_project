from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def sppeachtotext():
    return render_template('sppeachtotext.html')

if __name__ == '__main__':
    app.run(debug=True)

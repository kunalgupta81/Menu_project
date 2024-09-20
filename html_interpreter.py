from flask import Flask, render_template

app = Flask(__name__)

# Route for the live HTML interpreter page
@app.route('/')
def live_html_interpreter():
    return render_template('html_live_interpreter.html')

# Route for the home page (you can define your home content here)
@app.route('/home')
def home():
    return '''
        <html>
        <head><title>Home Page</title></head>
        <body>
            <h1>Welcome to the Home Page!</h1>
            <p>This is a simple Flask app that features a Live HTML Interpreter. Go back to the <a href="/">Interpreter</a>.</p>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

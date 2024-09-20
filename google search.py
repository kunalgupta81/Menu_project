from flask import Flask, render_template, request, redirect
import webbrowser

app = Flask(__name__)

# Route to serve the Google search page
@app.route('/')
def google_search():
    return render_template('google search.html')

# Route to handle the form submission
@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    google_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(google_url)  # Open the search in the default web browser
    return redirect('/')  # Redirect back to the search page

if __name__ == '__main__':
    app.run(debug=True)

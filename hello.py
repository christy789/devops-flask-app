from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """<h1>Home Page</h1>
        <a href="/about">About</a> |
        <a href="/contact">Contact</a> 
	<p>Hello, World! I am a Flask app!.</p>"""

@app.route("/about")
def about():
    return """h1>About Page</h1>
	    <p>This app is running on the Flask web framework. Read more at <a href="https://flask.palletsprojects.com/">Flask Documentation</a>.</p>
<a href="/">Home</a>""

@app.route("/contact")
def contact():
    return """
        <h1>Contact Page</h1>
        <p>Email: c12345678@mytudublin.ie</p>
        <a href="/">Home</a>
    """
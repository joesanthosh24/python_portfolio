# Flask is the Flask class and render_template is to render a template
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', name="Joe Santhosh")

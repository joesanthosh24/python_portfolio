# Flask is the Flask class and render_template is to render a template
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', name="Joe Santhosh")


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.form.to_dict()
    print(data)

    return render_template('index.html', msg='Thank You. Will respond soon')

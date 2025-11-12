from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route('/about')
def about():
    return 'Hello, World'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

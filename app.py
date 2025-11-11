from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"
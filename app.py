from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

# -----------------------------
# Mock user data (stored in code)
# -----------------------------
mock_user = {
    "username": "ktapia",
    "password": "pbkdf2:sha256:600000$0ziqO3u7sMmb1vlt$3990d36b8af49a0deedbb6918bb3b1a15fe75b60d4f040814cd22c775e8ff72c"   
    # hashed password
}


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


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

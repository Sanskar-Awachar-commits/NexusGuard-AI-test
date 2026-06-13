from flask import Flask, request, render_template_string
import os
import pickle
import sqlite3
import base64

app = Flask(__name__)
app.secret_key = "SUPER_SECRET_ADMIN_KEY_123"

@app.route('/ping')
def ping_host():
    ip = request.args.get('ip', '8.8.8.8')
    return "<pre>" + os.popen("ping -c 1 " + ip).read() + "</pre>"

@app.route('/hello')
def hello_user():
    name = request.args.get('name', 'Guest')
    template = f"<h1>Hello {name}!</h1>"
    return render_template_string(template)

@app.route('/load_session')
def load_session():
    data = request.args.get('data')
    if data:
        session_obj = pickle.loads(base64.b64decode(data))
        return f"Loaded session for {session_obj['user']}"
    return "No session data"

@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    user = cursor.fetchone()
    return str(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
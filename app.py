from flask import Flask
app = Flask(__name__)

from datetime import datetime
import os

env_var = os.environ

@app.route('/hello')
def hello_geek():
    return '<h1>Hello World</h2>'

@app.route('/time')
def currentTime():
    now = datetime.now()
    print(now)
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    return current_time

if __name__ == "__main__":
    print(env_var)
    port = env_var.get("PORT", 5001)
    app.run(debug=False, port=port)

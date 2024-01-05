from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello, I am Catherine and this is my Dockerized Flask App</h2>'


if __name__ == "__main__":
    # Use the dynamic port assigned by Heroku
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

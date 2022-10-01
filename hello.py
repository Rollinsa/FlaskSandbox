from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(f"REQUEST HERE: {request}")
    return "<p>Hello, World!</p>"
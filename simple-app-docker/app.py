import os
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Hello from: " + socket.gethostname() + "</h1>"

@app.route('/<name>')
def greeting(name):
    return "<h1>Hello, " + name + "</h1>"

if __name__ == "__main__":
    app.run()

import os
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>My Demo</h1>" + "<p>A Simple Python Application for testing purposes.</p>" + "<h3>Hello from: " + socket.gethostname() + "</h3>" + "<button>Button</button>"

@app.route('/<name>')
def greeting(name):
    return "<h3>Hello, " + name + "</h3>"

if __name__ == "__main__":
    app.run()

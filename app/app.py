from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from ECS via GitHub Actions CI/CD!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, send_from_directory

app = Flask(__name__)

VALIDATION_KEY = "c8a59a8e935f8abb56afb73e0d02b2"

@app.route("/")
def home():
    return "TokenAnalyzer Live"

@app.route("/validation-key.txt")
def validation():
    return VALIDATION_KEY

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

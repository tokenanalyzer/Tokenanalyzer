
from flask import Flask, Response
import os

app = Flask(__name__)

VALIDATION_KEY = "c8a59a8e935f8abb56afb73e0d02b2"

@app.route("/validation-key.txt")
def validation_key():
    return Response(VALIDATION_KEY, mimetype="text/plain")

@app.route("/")
def home():
    return "TokenAnalyzer Live"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

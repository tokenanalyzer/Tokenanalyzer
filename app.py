from flask import Flask, Response

app = Flask(__name__)

@app.route("/validation-key.txt")
def validation_key():
    return Response(
        "c8a59a8e935f8abb56afb73e0d02b2",
        mimetype="text/plain"
    )

@app.route("/")
def home():
    return "TokenAnalyzer Live"

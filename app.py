from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "TokenAnalyzer Live"

@app.route("/validation-key.txt")
def validate():
    return Response("c8a59a8e935f8abb56afb73e0d02b2", mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

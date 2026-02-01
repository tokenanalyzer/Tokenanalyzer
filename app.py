from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return "TokenAnalyzer Live"

@app.route("/validation-key.txt")
def validation():
    return send_from_directory(".", "validation-key.txt")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

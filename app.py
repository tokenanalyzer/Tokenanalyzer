from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "TokenAnalyzer Live"

@app.route("/validation-key.txt")
def validation():
    return Response(
        "c8a59a8e935f8abb56afb73e0d02b2",
        content_type="text/plain"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
@app.route("/validation-key.txt")
def validation_key():
    return "pi-domain-verification=c8a59a8e935f8abb56afb73e0d02b275a9b4b48cb7462b5b814cddc3a7fd35344d2d8d76f5c9a93324669f48a5c4f70ca09fa32a71a2e84674b084a04d28fca2", 200, {"Content-Type": "text/plain"}

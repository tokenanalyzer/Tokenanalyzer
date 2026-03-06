from flask import Flask

app = Flask(__name__)

VALIDATION_KEY = "c8a59a8e935f8abb56afb73e0d02b2"

# Home route
@app.route("/")
def home():
    return "TokenAnalyzer is running successfully"

# Validation file for Pi
@app.route("/validation-key.txt")
def validation():
    return VALIDATION_KEY

# Health check (Render ke liye useful)
@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

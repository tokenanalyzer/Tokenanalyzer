from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "TokenAnalyzer Flask Server is Running!"  # ✅ Properly indented return statement

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

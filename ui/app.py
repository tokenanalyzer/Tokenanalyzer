from flask import Flask, jsonify
import requests

app = Flask(__name__)

# 🔹 DexScreener API se data fetch karne ka function
def fetch_token_data():
    url = "https://api.dexscreener.com/latest/dex/tokens/0x..."
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {"error": "Failed to fetch data"}

@app.route('/api/token', methods=['GET'])
def get_token():
    data = fetch_token_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

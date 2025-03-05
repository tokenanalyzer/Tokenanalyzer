import requests

def fetch_token_data():
    pair_address = "A8nPhpCJqtqHdqUk35Uj9Hy2YsGXFkCZGuNwvkD3k7VC"  # Solana Pair Address
    url = f"https://api.dexscreener.com/latest/dex/pairs/solana/{pair_address}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pair = data.get("pair", None)
        if pair:
            print("✅ Token Data Found!")
            print(pair)  # Pura data print karega
        else:
            print("❌ No valid token data found!")
    else:
        print(f"⚠️ API request failed! Status Code: {response.status_code}")

# Function Run Karo
fetch_token_data()

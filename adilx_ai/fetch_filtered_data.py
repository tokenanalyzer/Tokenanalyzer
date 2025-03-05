import requests

def get_filtered_data():
    url = "https://api.dexscreener.com/latest/dex/tokens"  # Replace with actual API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Example filtering: High liquidity & trusted token check
        filtered_tokens = [
            token for token in data["tokens"]
            if token["liquidity"] >= 50000 and "scam" not in token["name"].lower()
        ]
        return filtered_tokens[0] if filtered_tokens else None

    return None

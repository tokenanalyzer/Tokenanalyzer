import requests
import json

def get_token_data(token_address):
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data, indent=4)
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    token_address = "6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN"
    print(get_token_data(token_address))

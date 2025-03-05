import requests
import json

# ✅ DexScreener API Se Data Fetch
url = "https://api.dexscreener.com/latest/dex/pairs/ethereum"
response = requests.get(url)

try:
    data = response.json()
    tokens = data.get("pairs", [])

    filtered_tokens = []

    for token in tokens:
        name = token.get("baseToken", {}).get("name", "Unknown")
        symbol = token.get("baseToken", {}).get("symbol", "Unknown")
        address = token.get("pairAddress", "N/A")
        chain = token.get("chainId", "N/A")
        price = token.get("priceUsd", "N/A")
        liquidity = token.get("liquidity", {}).get("usd", 0)
        volume_24h = token.get("volume", {}).get("h24", 0)
        price_change = token.get("priceChange", {}).get("h24", 0)
        holders = token.get("fdv", "N/A")

        # ✅ Risk Analysis
        risk_alerts = []
        if liquidity < 50000:
            risk_alerts.append("⚠️ Low Liquidity")
        if price_change < -30:
            risk_alerts.append("⚠️ Sudden Price Drop (-30%)")
        if volume_24h < 20000:
            risk_alerts.append("⚠️ Low Trading Volume")
        
        # ✅ Safe Token Condition (Avoid Scams)
        if liquidity >= 50000 and volume_24h >= 20000:
            filtered_tokens.append({
                "name": name,
                "symbol": symbol,
                "address": address,
                "chain": chain,
                "price": price,
                "liquidity": liquidity,
                "volume_24h": volume_24h,
                "price_change_24h": price_change,
                "risk_alerts": risk_alerts
            })

    # ✅ Final Output
    print(json.dumps(filtered_tokens, indent=4))

except json.JSONDecodeError:
    print("❌ API Response Invalid - JSON Decode Error")
except Exception as e:
    print(f"❌ Error: {e}")

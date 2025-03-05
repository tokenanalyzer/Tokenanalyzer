import cloudscraper
import json

DEX_API = "https://api.dexscreener.com/latest/dex/search?q=ETH"

scraper = cloudscraper.create_scraper()  # Cloudflare bypass
response = scraper.get(DEX_API)

print("🔄 API Response:", response.text)  # Debugging ke liye

try:
    data = response.json()
    print("✅ Valid Data Received!", json.dumps(data, indent=2))
except Exception as e:
    print("❌ JSON Decode Error:", e)

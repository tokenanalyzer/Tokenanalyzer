import requests

# ✅ Telegram Bot Details
BOT_TOKEN = "7503855575:AAFdRpB5M37ACH0asdZ_N87Yak8W1ajMHyA"
CHAT_ID = "1330261232"

# ✅ Token Data Fetch Karna
try:
    from fetch_filtered_data import get_filtered_data
    token_data = get_filtered_data()
except Exception as e:
    token_data = {"error": f"Failed to fetch data: {str(e)}"}

# ✅ Message Format
if "error" in token_data:
    message = f"❌ Error: {token_data['error']}"
else:
    message = f"✅ Token Alert!\n\n"
    message += f"🪙 Token: {token_data['Token']}\n"
    message += f"💰 Symbol: {token_data['Symbol']}\n"
    message += f"💲 Price: {token_data['Price']}\n"
    message += f"📊 Liquidity: {token_data['Liquidity']}\n"
    message += f"🏛 Market Cap: {token_data['Market Cap']}\n"
    message += f"📈 24h Change: {token_data['24h Change']}%\n"
    message += f"📉 Chart: {token_data['Chart']}"

# ✅ Telegram Message Send Karna
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": message}

response = requests.post(TELEGRAM_URL, json=payload)
if response.status_code == 200:
    print("✅ Message sent successfully!")
else:
    print(f"❌ Failed to send message: {response.text}")

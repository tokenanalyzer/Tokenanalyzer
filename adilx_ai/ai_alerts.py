import asyncio
import telegram
import requests

# Telegram Bot Credentials
BOT_TOKEN = "7503855575:AAFdRpB5M37ACH0asdZ_N87Yak8W1ajMHyA"
CHAT_ID = "1330261232"  # Adil Husain ka chat ID

# DexScreener API URL
DEX_API_URL = "https://api.dexscreener.com/latest/dex/tokens/"

async def send_telegram_message(bot, chat_id, message):
    """Telegram par message bhejne ke liye async function"""
    await bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")

def fetch_token_data(token_address):
    """Token data fetch karne ke liye function"""
    response = requests.get(DEX_API_URL + token_address)
    if response.status_code == 200:
        data = response.json()
        if data.get("pairs"):
            return data
        else:
            return None
    return None

async def main():
    token_address = "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6"  # Test ke liye token
    token_data = fetch_token_data(token_address)

    bot = telegram.Bot(token=BOT_TOKEN)

    if token_data:
        message = f"🚀 **Token Found!**\n🔹 **Token Address:** `{token_address}`"
    else:
        message = "❌ **Token not found on DexScreener!**"

    await send_telegram_message(bot, CHAT_ID, message)

# Async function execute karein
if __name__ == "__main__":
    asyncio.run(main())

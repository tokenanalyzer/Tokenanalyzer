import time
import json
from selenium import webdriver
import undetected_chromedriver as uc

# ✅ Headless Browser Setup for Cloudflare Bypass
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")

# ✅ Start Chrome Webdriver
driver = uc.Chrome(options=options)
url = "https://api.dexscreener.com/latest/dex/pairs/ethereum"

try:
    # ✅ Open API URL & Wait for Cloudflare to Bypass
    driver.get(url)
    time.sleep(5)  # Allow Cloudflare to process request

    # ✅ Extract API Response
    raw_response = driver.find_element("tag name", "pre").text
    print("✅ Raw API Response:")
    print(raw_response)

    # ✅ Parse JSON Response
    data = json.loads(raw_response)
    print("\n✅ Parsed JSON Output:")
    print(json.dumps(data, indent=4))

except json.JSONDecodeError:
    print("❌ JSON Error: Cloudflare Block - Try Running Again")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()  # Close browser

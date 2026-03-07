import requests
import time

TOKEN = "YOUR_TELEGRAM_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

PRODUCT_URL = "https://blinkit.com/prn/x/prid/754157"

cookies = {
    "gr_1_lat": "12.9041898",
    "gr_1_lon": "77.56597049999999",
    "gr_1_locality": "3"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive"
}

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
session = requests.Session()
session.headers.update(headers)

def check_stock():
    try:
        r = session.get(PRODUCT_URL, cookies=cookies, timeout=10)
        page = r.text.lower()

        print("Checking stock...")

        if "coming soon" in page:
            print("Coming soon")

        elif "out of stock" in page:
            print("Out of stock")

        elif "add to cart" in page:
            print("IN STOCK")
            send_telegram("🚨 Product IN STOCK on Blinkit!")
            return True

        else:
            print("Status unknown")

    except Exception as e:
        print("Error:", e)

    return False

while True:
    check_stock()
    time.sleep(3)
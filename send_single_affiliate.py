import pandas as pd
import random
import os
import requests

def send_affiliate_product():
    file_path = "amazon_affiliate_products.csv"
    if not os.path.exists(file_path):
        print(f"❌ קובץ {file_path} לא נמצא.")
        return

    df = pd.read_csv(file_path)
    df = df.dropna(subset=['link'])

    if df.empty:
        print("❌ אין מוצרים לשליחה.")
        return

    row = random.choice(df.to_dict(orient='records'))

    name = row.get("name", "Unknown Product")
    description = row.get("description", "")
    image_url = row.get("image_url", "")
    link = row.get("link")

    message = f"🔥 {name}

{description}

🔗 [צפה במוצר]({link})"

    send_to_telegram(message, image_url)

def send_to_telegram(message, image_url):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("❌ נא להגדיר את TELEGRAM_BOT_TOKEN ו-TELEGRAM_CHAT_ID בקובץ .env")
        return

    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    data = {
        "chat_id": chat_id,
        "caption": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=data, files={"photo": (image_url, requests.get(image_url).content)})
        print("✅ נשלח:", message[:40])
        print("סטטוס:", response.status_code)
    except Exception as e:
        print("❌ שגיאה בשליחה:", e)
import time
from send_single_affiliate import send_affiliate_product

def main():
    print("🤖 הבוט פועל! ישלח מוצר כל שעתיים.")
    while True:
        try:
            send_affiliate_product()
            print("🕒 המתנה לשעתיים...")
            time.sleep(2 * 60 * 60)  # המתנה של שעתיים
        except Exception as e:
            print(f"⚠️ שגיאה: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
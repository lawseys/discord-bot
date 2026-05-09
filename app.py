import requests
import threading
import time
import random
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Sistem Aktif"

CHANNEL_ID = os.getenv("1502688882343411866")
TOKEN = os.getenv("MTE4MDk3MTQwNDQ4OTkyNDczMA.Galkhw.CJugcTz9ZEOIjXNDBI6v3ovXwXUe-wald-bMQQ")
MESSAGE = "ÇINAR UMUT X HER DAİM SİKER ATİLLA KAYA FAMİLY"

def spam_at():
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
    while True:
        try:
            payload = {"content": f"{MESSAGE} | {random.randint(1000, 9999)}"}
            r = requests.post(url, headers=headers, json=payload, timeout=10)
            if r.status_code in [200, 201]:
                print("Gonderildi")
                time.sleep(6.5)
            elif r.status_code == 429:
                time.sleep(r.json().get('retry_after', 20) + 2)
            else:
                time.sleep(20)
        except:
            time.sleep(30)

if __name__ == "__main__":
    threading.Thread(target=spam_at, daemon=True).start()
    app.run(host='0.0.0.0', port=10000)

from flask import Flask
import threading
import os

app = Flask(__name__)

def run_bot():
    os.system("python bot.py")

@app.route('/')
def home():
    return "✅ Telegram bot ishlayapti!"

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

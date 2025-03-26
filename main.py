import telebot
import os
from flask import Flask, request

BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Або встав сюди токен напряму як рядок

bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "✅ Чек отримано! Починаю обробку...")

@app.route(f"/{BOT_TOKEN}", methods=['POST'])
def receive_update():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def home():
    return "Бот працює!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

import telebot
from telebot import types

TOKEN = "8231769343:AAFRn6Ht4IHydDrnM97bx8mXBuO-6GRw4_A"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎁 Получить подарок")
    btn2 = types.KeyboardButton("✉️ Подписаться на канал")
    btn3 = types.KeyboardButton("📢 Проверить подписку")
    btn4 = types.KeyboardButton("📝 Регистрация")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(
        message.chat.id,
        "Привет! 👋 Это бот Валентины.\nВыбери действие 👇",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "🎁 Получить подарок")
def send_gift(message):
    bot.send_message(message.chat.id, "Чтобы получить подарок 🎁, оставь свою почту ✉️")

@bot.message_handler(func=lambda message: message.text == "✉️ Подписаться на канал")
def subscribe_channel(message):
    bot.send_message(message.chat.id, "Подпишись на канал 👉 https://t.me/cashflow33Valentina")

@bot.message_handler(func=lambda message: message.text == "📢 Проверить подписку")
def check_subscription(message):
    bot.send_message(message.chat.id, "Проверка подписки пока включена вручную ✅")

@bot.message_handler(func=lambda message: message.text == "📝 Регистрация")
def registration(message):
    bot.send_message(message.chat.id, "Регистрация будет доступна позже 🔜")

bot.polling(none_stop=True)




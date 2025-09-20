import telebot
from telebot import types

# Вставь сюда свой токен от BotFather
TOKEN = "8231769343:AAEEG3pnc2ui9HgfP7cpdvDLTmvoLMcAfCk"
bot = telebot.TeleBot(TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # Приветственное сообщение
    bot.send_message(
        message.chat.id,
        "Привет! 👋 Это бот Валентины.\n\n"
        "Выбери действие 👇"
    )

    # Кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎁 Получить подарок")
    btn2 = types.KeyboardButton("📩 Проверить почту")
    btn3 = types.KeyboardButton("📢 Подписаться на канал")
    btn4 = types.KeyboardButton("📝 Регистрация")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, "Что хочешь сделать?", reply_markup=markup)


# Обработка кнопки "Получить подарок"
@bot.message_handler(func=lambda m: m.text == "🎁 Получить подарок")
def get_gift(message):
    bot.send_message(
        message.chat.id,
        "Введите свой e-mail, чтобы я могла отправить подарок 🎁.\n\n"
        "⚠️ Подарок отправляется вручную, поэтому, пожалуйста, подождите немного ⏳."
    )


# Обработка кнопки "Проверить почту"
@bot.message_handler(func=lambda m: m.text == "📩 Проверить почту")
def check_mail(message):
    bot.send_message(message.chat.id, "✉️ Пожалуйста, проверьте вашу почту (и папку Спам).")


# Обработка кнопки "Подписаться на канал"
@bot.message_handler(func=lambda m: m.text == "📢 Подписаться на канал")
def subscribe_channel(message):
    bot.send_message(
        message.chat.id,
        "Подписывайся на мой канал 👉 https://t.me/cashflow33Valentina"
    )


# Обработка кнопки "Регистрация"
@bot.message_handler(func=lambda m: m.text == "📝 Регистрация")
def registration(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn1 = types.InlineKeyboardButton("🇷🇺💰 Зарегистрироваться (₽)", url="https://potok.cash/ref/NBtMB6mq")
    btn2 = types.InlineKeyboardButton("🇨🇳💎 Зарегистрироваться (CNY)", url="https://duo6duo8.com/ref/dc9MSK6q")
    btn3 = types.InlineKeyboardButton("🇪🇺💶 Зарегистрироваться (EUR)", url="https://eur.cashflow.fund/ref/tSpMB6mq")

    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "💡 Хочешь зарабатывать вместе со мной?\nВыбирай сайт для регистрации 👇",
        reply_markup=markup
    )


# Запуск бота
bot.polling(non_stop=True)

import telebot

# ТВОЙ ТОКЕН
TOKEN = "8764558294:AAHqvNz45aw45PinXBEpzzSEANpje5UCiKk"  # ЗАМЕНИ!

# ФОРМУЛА ДЛЯ ГЕНЕРАЦИИ ПАРОЛЯ
# Здесь ты можешь написать ЛЮБУЮ формулу!
# Например: пароль = (сид * 2) / 2.375 * 3 / 10 * 1.23456789
def generate_password(sid):
    # ТВОЯ ФОРМУЛА - МЕНЯЙ КАК ХОЧЕШЬ!
    password = (sid * 2) / 2.375 * 3 / 10 * 5.23456789
    return round(password, 2)  # Округляем до 2 знаков

# МИНИМАЛЬНЫЙ И МАКСИМАЛЬНЫЙ СИД
MIN_SID = 10000
MAX_SID = 100000000

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "введите ваш сид указанный на экране"
    )

@bot.message_handler(content_types=['text'])
def generate(message):
    text = message.text.strip()
    chat_id = message.chat.id
    
    # ПРОВЕРЯЕМ - ЭТО ЧИСЛО?
    try:
        sid = float(text)
    except ValueError:
        bot.send_message(chat_id, "введите ваш сид")
        return
    
    # ПРОВЕРЯЕМ ДИАПАЗОН
    if sid < MIN_SID or sid > MAX_SID:
        bot.send_message(
            chat_id,
            f"введите ваш сид"
        )
        return
    
    # ГЕНЕРИРУЕМ ПАРОЛЬ
    password = generate_password(sid)
    
    # ВЫВОДИМ ТОЛЬКО ПАРОЛЬ!
    bot.send_message(
        chat_id,
        f"ваш пароль: {password}"
    )

print("запуск бота")
bot.infinity_polling()
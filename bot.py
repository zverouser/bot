import telebot

# Вставь свой токен
bot = telebot.TeleBot('8546565189:AAEKN9ZILyDe1xxeTzBhX_ewG1joFSCXc2c')


def clean_phone(raw_text):
    digits = ''.join([c for c in raw_text if c.isdigit()])

    if len(digits) == 10:
        # Сразу собираем готовую ссылку
        return f'https://t.me/+7{digits}'
    elif len(digits) == 11:
        if digits.startswith('7') or digits.startswith('8'):
            return f'https://t.me/+7{digits[1:]}'

    return None


@bot.message_handler(content_types=['text'])
def handle_message(message):
    result = clean_phone(message.text)

    if result:
        # Ссылка получится сразу кликабельная
        bot.reply_to(message, f"✅ Готово:\n{result}")
    else:
        bot.reply_to(message, "❌ Не нашёл номер в сообщении")


print("✅ Бот запустился")
bot.infinity_polling()
import telebot

# Дані експонатів
museum_data = {
    "EXP001": {
        "назва": "Мона Ліза",
        "автор": "Леонардо да Вінчі",
        "рік": "1503-1506",
        "опис": "Одна з найвідоміших картин у світі, зображення жінки з загадковою посмішкою."
    },
    "EXP002": {
        "назва": "Зоряна ніч",
        "автор": "Вінсент ван Гог",
        "рік": "1889",
        "опис": "Картина, що зображує нічне небо з вихрами світла і зірками."
    }
}

bot = telebot.TeleBot("7826632043:AAHESgJ2G718BkrBUS7lF28hmf2SFjV0pdE")

# Функція старту бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Вітаю! Я музейний гід. Введіть код експоната, щоб отримати інформацію про нього.")

# Функція для обробки введеного коду експоната
@bot.message_handler(func=lambda message: True)
def handle_code(message):
    code = message.text.strip().upper()  # Перетворюємо код на верхній регістр
    if code in museum_data:
        exhibit = museum_data[code]
        response = (
            f"Назва: {exhibit['назва']}\n"
            f"Автор: {exhibit['автор']}\n"
            f"Рік: {exhibit['рік']}\n"
            f"Опис: {exhibit['опис']}"
        )
    else:
        response = "Вибачте, експонат з таким кодом не знайдено. Перевірте правильність коду."
    bot.reply_to(message, response)

# Запускаємо бота
if __name__ == "__main__":
    bot.polling()

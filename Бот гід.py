# Імпортуємо необхідні бібліотеки
import json  # Для роботи з файлом JSON, де зберігається інформація про експонати
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Завантажуємо дані про експонати з файлу "museum_data.json"
with open("museum_data.json", "r", encoding="utf-8") as f:
    museum_data = json.load(f)  # Завантажуємо JSON як словник Python

# Функція, яка викликається, коли користувач вводить команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Вітаю! Я музейний гід. Введіть код експоната, щоб отримати інформацію про нього."
    )

# Функція для обробки повідомлення з кодом експоната
def handle_code(update: Update, context: CallbackContext) -> None:
    code = update.message.text.strip().upper()  # Перетворюємо код на великі літери
    # Перевіряємо, чи є код у базі даних
    if code in museum_data:
        exhibit = museum_data[code]
        # Формуємо відповідь з інформацією про експонат
        response = (
            f"Назва: {exhibit['назва']}\n"
            f"Автор: {exhibit['автор']}\n"
            f"Рік: {exhibit['рік']}\n"
            f"Опис: {exhibit['опис']}"
        )
    else:
        response = "Вибачте, експонат з таким кодом не знайдено. Перевірте правильність коду."
    # Відправляємо відповідь користувачу
    update.message.reply_text(response)

# Основна функція для запуску бота
def main():
    # Створюємо об'єкт Updater, який буде обробляти запити від Telegram
    updater = Updater("7826632043:AAHESgJ2G718BkrBUS7lF28hmf2SFjV0pdE", use_context=True)  # Замість YOUR_TELEGRAM_BOT_TOKEN вставте ваш токен
    dp = updater.dispatcher  # Dispatcher для обробки команд і повідомлень

    # Додаємо обробник команди /start
    dp.add_handler(CommandHandler("start", start))
    # Додаємо обробник звичайних текстових повідомлень (введення коду експоната)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_code))

    # Запускаємо бота
    updater.start_polling()
    updater.idle()

# Запуск бота, коли запускається цей файл
if __name__ == "__main__":
    main()

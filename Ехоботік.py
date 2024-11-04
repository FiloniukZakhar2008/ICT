import telebot

token='7687302010:AAH5TMjaqO6DHLs8VkBOCkWyFSv3CuSvOmU'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()

import telebot

bot = telebot.TeleBot("7992049935:AAG7-E3aYe1686GecjrBI8AdGRq2fTaRxrY")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت شغال وجاهز للتنفيذ.")

bot.polling()
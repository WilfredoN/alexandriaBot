import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def welcome_message(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    group1 = types.KeyboardButton("KI-310")
    group2 = types.KeyboardButton("KI-320")
    group3 = types.KeyboardButton("KI-330")
    markup.add(group1, group2, group3)
    bot.send_message(message.chat.id, text="Выберите свою группу: ", reply_markup=markup)
 
bot.polling(none_stop=True)
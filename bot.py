import telebot
from telebot import types
token = '5727842991:AAFe5RkAgdcEZtdFFcS7HxLIYJZAlj-GP5Y'
bot = telebot.Telebot(token)
@bot.message.handler(commands=['start'])
def welcome_message(message): 
    bot.send_message(message.chat.id, "Вас приветствует бот для напоминания о предстоящих парах, созданный студентом 3-го курса ХРТК!")
@bot.message.handler(commands=['button'])
def button_welcome(message):
    markup = types.ReplyKeyboardMarkup(resuze_keyboard=True)
    groups = [types.KeyboardButton("KI-310"), 
    types.KeyboardButton("KI-320"), 
    types.KeyboardButton("KI-330")]
    for i in groups: 
        markup.add(groups[i])





bot.infinity_polling()
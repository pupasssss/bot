import telebot
from telebot import types


bot = telebot.TeleBot("5462694930:AAEwAbrMBthewarPXeKz3qvc-ZFS-nMPX94", parse_mode=None)

#keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("герояв слава!")
item2 = types.KeyboardButton("давай по пивку")
markup.add(item1, item2)
	


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Слава Україні',parse_mode = 'html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id,'денег нет не вы держитесь')

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	if message.chat.type == 'private':
		if message.text == 'герояв слава!':
			bot.send_message(message.chat.id,'смерть ворогам!')
		elif message.text == 'давай по пивку':
			bot.send_message(message.chat.id, 'давай 🍻')


@bot.message_handler(func=lambda message: message.reply_to_message != None)
def reply_message_handler(message):
    bot.send_message(chat_id=message.reply_to_message.from_user.id, text=message.text)

bot.infinity_polling()

import telebot
from telebot import types

bot = telebot.TeleBot('6633816722:AAHNfvzxSAHzcuErW3x4PqmeLY1UGVlrJ4k')

@bot.message_handler(commands=['quiz'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    game = types.InlineKeyboardButton('PLAY NOW', url="https://t.me/piecesnetworkbot/apps")
    join = types.InlineKeyboardButton('JOIN NOW', url="https://t.me/piecesnetwork")
    website = types.InlineKeyboardButton('WEBSITE', url="https://pieces.network/web")
    twitter = types.InlineKeyboardButton('X', url="https://twitter.com/piecesnetwork")

    markup.add(game, join, website, twitter)

    bot.send_message(message.chat.id, 'Free to Play\n\nPlay now and claim your reward', reply_markup=markup)

# Jalankan bot
bot.polling()

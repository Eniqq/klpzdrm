import types
import telebot
import sqlite3

bot = telebot.TeleBot('7847762596:AAEMw7ZvrMK21vSjZUTvrF6f0byVCjP-joE')  # Замени 'YOUR_BOT_TOKEN' на свой токен бота


# Обработка команд /hpmabase и /hpmawiki
@bot.message_handler(commands=['hpmabase', 'hpmawiki'])
def site(message):
    bot.send_message(message.chat.id, 'https://enshrined-creek-f7e.notion.site/Harry-Potter-magic-awakened-5fe808d27536425980fcb3f1f1e13d4b')

# Обработка команд /kang и /канг ютуб
@bot.message_handler(commands=['kang', 'канг'])
def site(message):
    bot.send_message(message.chat.id, 'https://www.youtube.com/@SmallKangKang')

# Обработка команд /main, /hello
@bot.message_handler(commands=['main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Kelpizdrim')

# Обработка текстовых запросов
@bot.message_handler()
def info(message):
    text = message.text.lower()

    if text == 'драмиона':
        bot.send_message(message.chat.id, 'канон')
    elif text == 'страница':
        bot.send_message(message.chat.id, '394')
    elif text == 'картоха':
        bot.send_message(message.chat.id, 'топыч')
    elif text == 'гослинг':
        bot.send_message(message.chat.id, 'да не умер он в конце фильма!')
    elif text == 'wb':
        bot.send_message(message.chat.id, 'контора опездолов')
    elif text == '10 очков':
        bot.send_message(message.chat.id, 'Слизерину!')
    elif text == 'kang':
        bot.send_message(message.chat.id, 'https://www.youtube.com/@SmallKangKang')
    elif text == 'hpmabase' or text == 'hpmawiki':
        bot.send_message(message.chat.id, 'https://enshrined-creek-f7e.notion.site/Harry-Potter-magic-awakened-5fe808d27536425980fcb3f1f1e13d4b')

bot.infinity_polling(none_stop=True)

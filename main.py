import telebot
all_words = ['тупой', 'даун']
bot = telebot.TeleBot('5677797764:AAEoLJ2VjmWKwbqplsJpwg_8htOjsjOuuBw')
@bot.message_handler(content_types=['text'])
def start_message(message):
    user_id = message.from_user.id
    if message.text == 'нет': bot.send_message(user_id, 'ДА')
    elif message.text == 'привет': bot.send_message(user_id, f'Привет {message.from_user.first_name}')
    elif message.text == 'спор': bot.send_message(user_id, 'Процесс отстаивания каждой из сторон своего мнения, столкновение мнений и попытки убедить оппонента. Большинство споров оканчиваются компромиссом. Спор это когда два или более оппонентов заявили об этом друг другу, иначе это не спор, а диалог')
    elif message.text in all_words: bot.send_message(user_id, f'ты {message.text}')
    else: bot.send_message(user_id, message.text)
bot.polling()
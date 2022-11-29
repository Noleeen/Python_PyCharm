import telebot
import json

API_TOKEN = '5871471859:AAGh_a7txmMqHad6hzVWpnc7cVoQ636ZJ7w'

bot = telebot.TeleBot(API_TOKEN)

films = []

def save():
    with open("films.json", 'w', encoding= 'utf-8') as f:
        f.write(json.dumps(films, ensure_ascii=False))
    print("сохранено")

def load():
    global films
    with open("films.json", 'r', encoding= 'utf-8') as f:
        films = json.load(f)
    print("загружено")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'пойдём')
# Декоратор @message_handler реагирует на входящие сообщение.
# Message – это объект из Bot API, содержащий в себе информацию о сообщении. Полезные поля:
# message.chat.id – идентификатор чата
# message.from.id – идентификатор пользователя
# message.text – текст сообщения
# Функция send_message принимает идентификатор чата (берем его из сообщения) и текст для отправки.
    try:
        load()
        bot.send_message(message.chat.id, 'фильмотека загружена')
    except:
        films.append('oodin')
        films.append('dva')
        bot.send_message(message.chat.id, 'загружено по умолчанию')

@bot.message_handler(commands=['все'])
def start_message(message):
    bot.send_message(message.chat.id,' '.join(films))

@bot.message_handler(commands=['calc']) # запрос в одну строчку с командой
def calc_message(message):
    eq = message.text.split()
    bot.send_message(message.chat.id, eval(eq[1]))


@bot.message_handler(commands=['c'])
def calc_message(message):
    eq = message.text.split()
    bot.send_message(message.chat.id, eval(eq[1]))

@bot.message_handler(content_types='text') # обработка ботом тестовой информации
def messag_reply(message):
    if 'привет' in message.text:
        bot.send_message(message.chat.id,'соберись уже!')


bot.polling()
import telebot
from telebot import types
from config_r import config
import game
import random
from calc import operator, complex, log


bot = telebot.TeleBot(token= config.bot_token.get_secret_value())

kb_calc = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Rational_numbers')
btn2 = types.KeyboardButton('Complex_numbers')
btn3 = types.KeyboardButton('Log')
btn4 = types.KeyboardButton('Exit')
kb_calc.add(btn1,btn2,btn3, btn4)

def list_print(a):
    l = f'''
{a[0][0]}  {a[0][1]}  {a[0][2]}
{a[1][0]}  {a[1][1]}  {a[1][2]}
{a[2][0]}  {a[2][1]}  {a[2][2]}
    '''
    return l

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    bt1 = types.KeyboardButton('game')
    bt2 = types.KeyboardButton('calc')
    markup.add(bt1, bt2)
    msg = bot.send_message(message.chat.id,'hello, human. would you like game game or calc?',
                     reply_markup= markup)
    bot.register_next_step_handler(msg, choice)

def choice(message):
    if message.text == 'game':
        global r
        global move
        global ch
        global count
        global array
        r = random.randint(0, 1)
        move = 'X'
        ch = True
        count = 0
        array = game.ar(3)
        markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        bt3 = types.KeyboardButton('go')
        markup2.add(bt3)
        bot.send_message(message.chat.id, 'go?',
                         reply_markup= markup2)
        # bot.register_next_step_handler(msg2, games)
    elif message.text == 'calc':

        msg2 = bot.send_message(message.chat.id, 'ok, enter option',
                                reply_markup=kb_calc)
        bot.register_next_step_handler(msg2, calc)

def games(message):
    bot.send_message(message.chat.id,'eqwedfq ')


@bot.message_handler(content_types='text')
def games2(message):

    global r
    global move
    global ch
    global count
    global array

    if message.text == 'go':
        while ch:
            # count_1 = (array[0]+array[1]+array[2]).count('-')
            # count_2 = (array[0]+array[1]+array[2]).count('-')
            bot.send_message(message.chat.id,list_print(array))
            if r:
                # while count_1 == count_2:

                # msg2 = bot.send_message(message.chat.id, 'enter row and column via space ')
                # bot.register_next_step_handler(msg2, temp)
                # row = message.text
                # step = [int(row[0]), int(row[2])]

                bot.send_message(message.chat.id, 'enter row and column via space')
                count += 1
                text = message.text
                array[int(text[0]) - 1][int(text[1]) - 1] = move
                    # count_2 = (array[0]+array[1]+array[2]).count('-')
            else:
                moveC = game.comp(array)
                array[moveC[0]][moveC[1]] = move

            r = not r
            count += 1
            if count > 4:
                winner = game.win(array)
                if winner == 1:
                    bot.send_message(message.chat.id,list_print(array))
                    if move == 'X':
                        bot.send_message(message.chat.id,'congratulation! winner X ')
                    else:
                        bot.send_message(message.chat.id,'congratulation! winner O ')
                    break
                elif winner == 2:
                    bot.send_message(message.chat.id,list_print(array))
                    bot.send_message(message.chat.id,'game over. no winner')
                    break
            if move == 'X':
                move = 'O'
            else:
                move = 'X'

def calc(message):
    if message.text == 'Rational_numbers':
        msg2 = bot.send_message(message.chat.id, 'ok, enter your expression')
        bot.register_next_step_handler(msg2, calc_rational)
    elif message.text == 'Complex_numbers':
        msg2 = bot.send_message(message.chat.id, 'ok, enter your expression')
        bot.register_next_step_handler(msg2, calc_complex)
    elif message.text == 'Log':
        logger = open('log.txt', 'r')
        msg = bot.send_message(message.chat.id, logger,reply_markup= kb_calc)
        bot.register_next_step_handler(msg, calc)
    elif message.text == 'Exit':
        close = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Goodbye',reply_markup=close)


def calc_complex(message):
    l = message.text
    res = complex(l)
    msg = bot.send_message(message.chat.id, res, reply_markup= kb_calc)
    log(message.text, res)
    bot.register_next_step_handler(msg, calc)

def calc_rational(message):
    l = message.text
    l = l.replace(' ', '')
    l = ' ' + l + ' '

    while '(' in l:
        ind_1 = l.find('(')
        ind_2 = l.find(')')
        l_temp = ' ' + l[ind_1 + 1: ind_2] + ' '
        l_temp = operator(operator(operator(operator(l_temp, '*'), '/'), '+'), '-')
        l_temp = l_temp.replace(' ', '')
        l = l[:ind_1] + l_temp + l[ind_2 + 1:]

    res = operator(operator(operator(operator(l, '*'), '/'), '+'), '-')
    msg = bot.send_message(message.chat.id, res, reply_markup= kb_calc)
    log(message.text, res)
    bot.register_next_step_handler(msg, calc)

print('I\'m running!')
bot.polling()
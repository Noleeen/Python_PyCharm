import telebot
from config_r import config
import game
import random


bot = telebot.TeleBot(token= config.bot_token.get_secret_value())


def list_print(a):
    l = f'''
{a[0][0]}  {a[0][1]}  {a[0][2]}
{a[1][0]}  {a[1][1]}  {a[1][2]}
{a[2][0]}  {a[2][1]}  {a[2][2]}
    '''
    return l

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'hello, human. would you like game (/game) or (/calc)?')

@bot.message_handler(commands=['game'])
def game_com(message):
    bot.send_message(message.chat.id, 'start?')

@bot.message_handler(content_types='text')
def play(message):
        r = random.randint(0, 1)
        array = game.ar(3)
        ch = True
        move = 'X'
        count = 0
        while ch:
            count_1 = (array[0]+array[1]+array[2]).count('-')
            count_2 = (array[0]+array[1]+array[2]).count('-')
            bot.send_message(message.chat.id,list_print(array))

            if r:
                while count_1 == count_2:
                    @bot.message_handler()
                    def user_move(message):
                        bot.send_message(message.chat.id, 'enter row and column via space ')
                        row = message.text
                        step = [int(row[0]), int(row[2])]

                        # def ch3(ar):
                        #     c = 0
                        #     while not c:
                        #         f = input_u()
                        #         if 0 < f[0] < 4 and 0 < f[1] < 4:
                        #             if ar[f[0] - 1][f[1] - 1] == '-':
                        #                 c = 1
                        #             else:
                        #                 print('this cell is busy, move in free cell ')
                        #
                        #         else:
                        #             print('error enter! repeat,l enter')
                        #     return f

                        array[step[0] - 1][step[1] - 1] = move
                        count_2 = (array[0]+array[1]+array[2]).count('-')
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





bot.polling()
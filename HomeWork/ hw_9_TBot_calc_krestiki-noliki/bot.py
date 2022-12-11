from aiogram import Bot,Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from config_r import config
import nolik

import time
import random


bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)

kb_main = ReplyKeyboardMarkup(resize_keyboard= True)
kb_main.add('/calc').insert('/X_and_0')

kb_xo = ReplyKeyboardMarkup(resize_keyboard= True)
kb_xo.add('/play_with_bot').insert('/2_players')

kb_xo_play = ReplyKeyboardMarkup(resize_keyboard= True)
kb_xo_play.add('/0').insert('/1').insert('/2').add('/3').insert('/4').insert('/5').add('/6').insert('/7').insert('/8')


game_list = ['-'] * 9

def list_print(l):
    l = f'''
{game_list[0]}  {game_list[1]}  {game_list[2]}
{game_list[3]}  {game_list[4]}  {game_list[5]}
{game_list[6]}  {game_list[7]}  {game_list[8]}
    '''
    return l
async def on(_):
    print('bot is runing')

@dp.message_handler(commands=['start'])
async def com_start(message: types.Message):
    await message.answer('hello, human.', reply_markup= kb_main)

@dp.message_handler(commands=['X_and_0'])
async def com_X(message: types.Message):
    await message.answer('with whom are you going play?', reply_markup= kb_xo)


@dp.message_handler(commands=['2_players'])
async def com_2_players(message: types.Message):
    await message.answer('sorry, this option is in developing')

@dp.message_handler(commands=['play_with_bot'])
async def com_play_with_bot(message: types.Message):
    await message.answer('ok, let\'s go!',reply_markup= kb_xo_play)
    r = random.randint(0, 1)
    check = 0
    move = 'X'
    while not check:
        if r:
            time.sleep(10)
            # await message.answer(list_print(game_list), reply_markup=kb_xo_play)

            @dp.message_handler(commands=['/0'])
            async def com_0(message: types.Message):
                game_list[0] = move
                # await message.delete()
                await message.answer(list_print(game_list))
            @dp.message_handler(commands=['/1'])
            async def com_1(message: types.Message):
                game_list[1] = move
                # await message.delete()
                await message.answer(list_print(game_list))
        else:
            game_list[nolik.comp(game_list)] = move
            await message.answer(list_print(game_list))
        if move == 'X':
            move = '0'
        else:
            move = 'X'
        r = not r

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on, skip_updates= True)
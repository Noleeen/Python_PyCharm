from aiogram import Bot,Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from config_r import config

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)

kb_main = ReplyKeyboardMarkup(resize_keyboard= True)
kb_main.add('/calc').insert('/X_and_0')

kb_xo = ReplyKeyboardMarkup(resize_keyboard= True)
kb_xo.add('/play_with_bot').insert('/2_players')
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
    await message.answer('ok, let\'s go!')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on, skip_updates= True)
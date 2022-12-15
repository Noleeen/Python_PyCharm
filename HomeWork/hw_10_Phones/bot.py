import telebot
from config import config

bot = telebot.TeleBot(token=config.bot_token.get_secret_value())



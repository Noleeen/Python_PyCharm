import telebot

import function as f


from config import config
import keyboards as k

bot = telebot.TeleBot(token=config.bot_token.get_secret_value())

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.send_message(message.chat.id, 'Welcome to the phone book!',
                           reply_markup=k.kb_menu)
    bot.register_next_step_handler(msg, main_menu)

def main_menu(message):
    if message.text == 'All contacts':
        data_json = f.read_data('phones.json')
        all = f.print_all(data_json)
        msg = bot.send_message(message.chat.id, all,
                               reply_markup=k.kb_menu)
        bot.register_next_step_handler(msg, main_menu)
    elif message.text == 'New contact':
        new = 'Введите через пробел имя, телефон, адрес, дату рождения, эл. почту '
        msg = bot.send_message(message.chat.id, new,
                               reply_markup=k.kb_menu)
        bot.register_next_step_handler(msg, new_contact)
    elif message.text == 'Find':
        new = 'Введите имя'
        msg = bot.send_message(message.chat.id, new)
        bot.register_next_step_handler(msg, find_contact)
    elif message.text == 'Edit contact':
        new = 'Введите имя'
        msg = bot.send_message(message.chat.id, new)
        bot.register_next_step_handler(msg, view_edit_contact)
    elif message.text == 'Delete contact':
        pass
    elif message.text == 'Exit':
        bot.send_message(message.chat.id, 'see you again',
                         reply_markup=k.close)


def new_contact(message):
    l = message.text.split()
    data_json = f.read_data('phones.json')
    new_id = f.generate_id(data_json)
    f.add_new(data_json, 'phones.json', l, new_id)
    msg = bot.send_message(message.chat.id, 'Новый контакт добавлен',
                           reply_markup=k.kb_menu)
    bot.register_next_step_handler(msg, main_menu)

def find_contact(message):
    l = message.text
    data_json = f.read_data('phones.json')
    find = f.find(data_json, l)
    msg = bot.send_message(message.chat.id, find, parse_mode = "HTML",
                           reply_markup=k.kb_menu)
    bot.register_next_step_handler(msg, main_menu)

def view_edit_contact(message):
    l = message.text
    data_json = f.read_data('phones.json')
    edit = f.edit(data_json, l)
    msg = bot.send_message(message.chat.id, f'скопируйте, проведите редактирование и нажмите ввод:\n {edit}',
                           )
    bot.register_next_step_handler(msg, edit_contact)


def edit_contact(message):
    l = message.text.split()
    data_json = f.read_data('phones.json')
    new_id = data_json[l[0]]['id']
    f.add_new(data_json, 'phones.json', l, new_id)
    msg = bot.send_message(message.chat.id, 'изменения сохранены',
                           reply_markup=k.kb_menu)
    bot.register_next_step_handler(msg, main_menu)




print('I am working =)')
bot.polling()
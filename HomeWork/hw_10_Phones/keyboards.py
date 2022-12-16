from telebot import types

close = types.ReplyKeyboardRemove(selective=False)

kb_del = types.ReplyKeyboardMarkup(resize_keyboard=True)
b1 = types.KeyboardButton('Yes')
b2 = types.KeyboardButton('No')
kb_del.add(b1,b2)


kb_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('All contacts')
btn6 = types.KeyboardButton('New contact')
btn2 = types.KeyboardButton('Find')
btn3 = types.KeyboardButton('Edit contact')
btn4 = types.KeyboardButton('Delete contact')
btn5 = types.KeyboardButton('Exit')
kb_menu.add(btn1,btn6)
kb_menu.add(btn2,btn3,btn4)
kb_menu.add(btn5)

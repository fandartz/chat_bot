from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('Сделать заказ')
btn2 = KeyboardButton('Дата готовности заказа')
btn3 = KeyboardButton('Узнать наличие товара')
btn4 = KeyboardButton('Актуальный прайс-лист')
btn5 = KeyboardButton('Наш адрес и режим работы')
btn6 = KeyboardButton('Связаться с менеджером')
Menu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn1, btn2, btn3, btn4, btn5, btn6)
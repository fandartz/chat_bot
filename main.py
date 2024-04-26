from markup import Menu
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TOKEN = 'token' #токен бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

chat_id=11111

#Запуск бота
@dp.message_handler(commands=['start'])
async def bot_message(message: types.Message):
    #
    await bot.send_message(message.chat.id, f"Здравствуйте ! Я робот помощник Сильвер Студио . На этой странице вы можете быстро получить ответ на 99 процентов вопросов . Если здесь нет нужного вам вопроса , то напишите нам в чат и мы вам ответим -)", reply_markup=Menu)


#Ответ на "Сделать заказ"
@dp.message_handler(text=['Сделать заказ'])
async def user_register(message: types.Message):
    await bot.send_message(message.chat.id, f"Благодарим Вас за заказ ! . Просим вас оформить его на сайте по ссылке: https://silverstudio.moscow/order. В мессенджерах заказы не принимаем. Благодарим за понимание -:)", reply_markup=Menu)

#Ответ на "дата готовности"
@dp.message_handler(text=['Дата готовности заказа'])
async def user_register(message: types.Message):
    await bot.send_message(message.chat.id, f"Здравствуйте! Все наши ткани производятся на заказ. Стандартный срок производства 12-14 дней после оплаты заказа. Вы можете самостоятельно посчитать дату готовности прибавив 14 дней к дате вашей оплаты. Если заказ будет готов раньше ( такое часто бывает ) мы вас проинформируем об этом.", reply_markup=Menu)

#Ответ на "узнать наличие"
@dp.message_handler(text=['Узнать наличие товара'])
async def user_register(message: types.Message):
    await bot.send_message(message.chat.id, f"Все наши ткани производятся на заказ. Стандартный срок производства 12-14 дней после оплаты заказа. В наличии готовых тканей не держим . Если заказ будет готов раньше ( такое часто бывает ) мы вас проинформируем об этом.", reply_markup=Menu)

#Ответ на "актуальный прайс-лист"
@dp.message_handler(text=['Актуальный прайс-лист'])
async def user_register(message: types.Message):
    await bot.send_message(message.chat.id, f"Текущий рекомендованный розничный  прайс-лист опубликован на нашем сайте: https://silverstudio.moscow/actual-price-list. Чтобы обсудить условия по скидкам звоните +7(995)112-20-23", reply_markup=Menu)

#Ответ на "режим работы"
@dp.message_handler(text=['Наш адрес и режим работы'])
async def user_register(message: types.Message):
    await bot.send_message(message.chat.id, f"Наш шоу-рум находится в Москве, по адресу г. Москва, ул.Рябиновая, дом 41 к 1 стр.2, Дизайн Центр Мадекс, 2-й этаж. Ссылка на карту: https://yandex.ru/maps/-/CDVaIG99. Мы открыты для посещения в рабочие дни, с 12 до 18 часов по предварительной договоренности. Пожалуйста согласовывайте свой визит заранее по телефону +7(995)112-20-23", reply_markup=Menu)

#Ответ на "жалобы и предложения"
@dp.message_handler(text=['Связаться с менеджером'])
async def user_register(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('связаться с менеджером', url='https://t.me/silverstudiomoscow')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
    await bot.send_message(message.chat.id, f"Если у вас есть пожелания, комментарии или жалобы вы можете связаться с менеджером:", reply_markup=inline_kb1)

#Кнопка отмены в жалобах
@dp.message_handler(text=['Отмена'])
async def user_register(message: types.Message):
    await bot.send_message(message.chat.id, f"Здравствуйте ! Я робот помощник Сильвер Студио . На этой странице вы можете быстро получить ответ на 99 процентов вопросов . Если здесь нет нужного вам вопроса , то напишите нам в чат и мы вам ответим -)", reply_markup=Menu)

#Любой другой текст, которого нет в списке
@dp.message_handler(content_types=['any'])
async def user_register(message: types.Message):
    await bot.forward_message(chat_id=chat_id, from_chat_id=message.chat.id, message_id=message.message_id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,)
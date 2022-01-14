from aiogram import types
from setup import dp
from keyboards.kb_client import client_start_keyboard

'''Handlers for other part of application'''


@dp.message_handler(content_types=['text'])
async def echo_msg(message: types.Message):
    if '/' in message.text[0]:
        await message.answer('Эта команда мне неизвестна...\n'
                             'Вы были возвращены в главное меню.',
                             reply_markup=client_start_keyboard)
    else:
        await message.answer('Я вас не понимаю...\n'
                             'Вы были возвращены в главное меню.',
                             reply_markup=client_start_keyboard)

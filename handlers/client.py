from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from setup import dp, bot
from keyboards.kb_client import client_start_keyboard, client_ask1_keyboard, client_ask2_keyboard, client_ask3_keyboard

'''Handlers for client part of application'''


class FSMClient(StatesGroup):
    size = State()
    payment_method = State()
    confirm = State()


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               'Время заказывать пиццу!\n'
                               'Для этого вы можете пользоваться меню :)'
                               , reply_markup=client_start_keyboard)
    except:
        await message.reply('Бот отвечает только в личные сообщения.\n'
                            'Для этого добавьте его по тегу @kvint_solution_bot')


@dp.message_handler(commands=['help'])
async def on_help(message: types.Message):
    await message.answer('В этом боте с помощью клавишы "Я хочу заказать пиццу!" можно оформить заказ.')


@dp.message_handler(Text(equals='Я хочу заказать пиццу!'), state=None)
async def order_pizza(message: types.Message):
    await FSMClient.size.set()
    await message.reply(f'Здравствуйте, {message.from_user.first_name}.\n'
                        f'Какую пиццу вы хотите? Большую или маленькую?',
                        reply_markup=client_ask1_keyboard)


@dp.message_handler(lambda message: message.text == 'Большая' or message.text == 'Маленькая', state=FSMClient.size)
async def set_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await FSMClient.next()
    await message.reply('Как вы будете платить? Наличными или картой?',
                        reply_markup=client_ask2_keyboard)


@dp.message_handler(lambda message: message.text == 'Наличные' or message.text == 'Карта', state=FSMClient.payment_method)
async def set_payment_method(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['payment_method'] = message.text
    await FSMClient.next()
    await message.reply(f'Ваша пицца: {data.get("size")}.\n'
                        f'Тип оплаты: {data.get("payment_method")}.\n'
                        f'Все правильно?',
                        reply_markup=client_ask3_keyboard)


@dp.message_handler(lambda message: message.text == 'Да' or message.text == 'Нет', state=FSMClient.confirm)
async def set_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['confirm'] = message.text[0:]
    if message.text == 'Да':
        await message.answer('Спасибо за заказ! Вы были возращены в главное меню.',
                             reply_markup=client_start_keyboard)
    else:
        await message.answer('Вы были возвращены в главное меню для того, чтобы вы могли отредактировать свой заказ.',
                             reply_markup=client_start_keyboard)

    await state.finish()
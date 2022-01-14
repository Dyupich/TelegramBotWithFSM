from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_order_pizza = KeyboardButton('Я хочу заказать пиццу!')
client_start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

button_ask1_big = KeyboardButton('Большая')
button_ask1_small = KeyboardButton('Маленькая')
client_ask1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

button_ask2_cash = KeyboardButton('Наличные')
button_ask2_card = KeyboardButton('Карта')
client_ask2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

button_ask3_yes = KeyboardButton('Да')
button_ask3_no = KeyboardButton('Нет')
client_ask3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

client_start_keyboard.add(button_order_pizza)
client_ask1_keyboard.row(button_ask1_big, button_ask1_small)
client_ask2_keyboard.row(button_ask2_cash, button_ask2_card)
client_ask3_keyboard.row(button_ask3_yes, button_ask3_no)

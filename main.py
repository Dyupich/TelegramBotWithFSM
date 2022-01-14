from aiogram.utils import executor
from setup import dp
from handlers import admin, client, other


async def on_startup(_):
    print('Бот запущен!')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=on_startup)

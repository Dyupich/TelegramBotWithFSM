from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "5082628845:AAF7JiCYGgotXq55C_GNLC73RvwhPdE3PiQ"
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config_data import config
from aiogram import Bot


storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

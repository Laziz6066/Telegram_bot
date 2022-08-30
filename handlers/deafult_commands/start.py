from aiogram.types import Message
from loader import dp, bot
from aiogram import types, Dispatcher


async def bot_start(message: Message):
    await message.reply(f"Привет {message.from_user.full_name}! Я Трэвэл бот.\nЧтобы узнать "
                        f"мои команды напишите /help")


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
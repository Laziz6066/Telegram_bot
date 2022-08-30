from loader import dp
from aiogram.types import Message
from aiogram import types, Dispatcher


async def bot_echo(message: Message):
    await message.reply(f'Эхо без состояния или фильтра.\nСообщение: {message.text}')


def register_handler_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo, state=None)
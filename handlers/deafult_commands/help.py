from aiogram.types import Message
from loader import dp
from config_data.config import DEAFULT_COMMANDS
from aiogram import types, Dispatcher


async def bot_help(message: Message):
    text =[f'/{command} - {desk}' for command, desk in DEAFULT_COMMANDS]
    await message.reply('\n'.join(text))


def register_handler_help(dp: Dispatcher):
    dp.register_message_handler(bot_help, commands=['help'])
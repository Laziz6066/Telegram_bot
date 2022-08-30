from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp, bot
from aiogram import types, Dispatcher
from states import storage


async def city(message: Message, state: storage.FSMContext):
    await message.answer('Введите город где будет проводиться поиск')
    await storage.UserState.name.set()



def register_lowprice(dp: Dispatcher):
    dp.register_message_handler(city, commands='lowprice')


storage.register_storage_adress(dp)
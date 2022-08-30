from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config_data import config
from loader import dp
from aiogram import types, Dispatcher
import tracemalloc, requests, json, lxml
from bs4 import BeautifulSoup
from keyboards.reply import re_keyboard
from keyboards.inline import in_keyboard

tracemalloc.start()


class UserState(StatesGroup):
    name = State()


async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    querystring = {"query": {data['name']}, "locale": "en_US", "currency": "USD"}
    response = requests.get(url=config.URL, headers=config.headers,  params=querystring)
    data = json.loads(response.text)
    for i in data['suggestions'][0]['entities']:
        in_keyboard.low_inlkb.add(in_keyboard.InlineKeyboardButton(
            text=BeautifulSoup(i['caption'], 'lxml').text, callback_data=in_keyboard.count))

    await message.answer('Уточните пожалуйста локацию:', reply_markup=in_keyboard.low_inlkb)


    await state.finish()


def register_storage_adress(dp: Dispatcher):
    dp.register_message_handler(get_address, state=UserState.name)
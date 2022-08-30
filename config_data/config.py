import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл: .env')
else:
    load_dotenv()


BOT_TOKEN = os.getenv('TOKEN')
headers = {
	"X-RapidAPI-Key": "f453754dc6mshcc6ce7b5c35ab92p14da94jsnd6111dae14be",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"}
URL = os.getenv('URL')

DEAFULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Вывести справку'),
    ('lowprice', 'Узнать топ самых дешёвых отелей в городе'),
    ('highprice', 'Узнать топ самых дорогих отелей в городе'),
    ('bestdeal', 'Узнать топ отелей, наиболее подходящих по цене и расположению от центра'),
    ('history', 'Узнать историю поиска отелей')
)

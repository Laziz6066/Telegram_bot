from aiogram.utils import executor
from loader import dp
from handlers.deafult_commands import echo, start, help
from handlers.hotels_commands import lowprice, highprice, bestdeal, history


async def on_startup(_):
    print('Бот вышел в онлайн')

start.register_handler_start(dp)
help.register_handler_help(dp)
lowprice.register_lowprice(dp)




echo.register_handler_echo(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

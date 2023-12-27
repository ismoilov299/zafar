from aiogram.dispatcher.filters import CommandStart
from aiogram.types import *
from loader import dp


@dp.message_handler(CommandStart())
async def command_start(msg: Message):
    await msg.reply(f"Привет {msg.from_user.full_name} добро пожаловать в бот. \n"
                    f"Просто напишите мне название песни, отрывок или короткое видео, и я найду это для вас.\n"
                    f"Нажмите команду /top, чтобы загрузить популярные песни в Узбекистане.")
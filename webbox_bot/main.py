
from aiogram import Dispatcher, Bot, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters.command import Command
import asyncio
import logging
from config import *

bot = Bot(token='7248104392:AAFR4NDI3fnwZ6VVpx54KxOBq2A0EH4K-SY')
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(msg: types.Message):
    markup = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Открыть", web_app=WebAppInfo(url=BASE_URL))]])
    await msg.answer("Привет!", reply_markup=markup)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

from aiogram import Dispatcher, Bot, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters.command import Command
import asyncio
import logging
from config import *
import requests

bot = Bot(token='7248104392:AAFR4NDI3fnwZ6VVpx54KxOBq2A0EH4K-SY')
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(msg: types.Message):
    await msg.answer("Привет! Я бот для взаимодействия с платформой Webbox! Чтобы начать нажми на кнопку 'Начать'!")

@dp.message(Command('author'))
async def cmd_start(msg: types.Message):
    await msg.answer("Автор телеграм бота: Никита Федосов")


@dp.message(Command('help'))
async def cmd_start(msg: types.Message):
    await msg.answer("/start - приветственное сообщение\n/author - автор проекта\n/help - помощь")

@dp.message(Command('status'))
async def cmd_start(msg: types.Message):
    r = requests.get('https://webbox.paia1nik.com/api/v2/status')
    if r.status_code == 200:
        response = r.json()
        print(response)
    await msg.answer(f"Сервер: {response}")
    



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
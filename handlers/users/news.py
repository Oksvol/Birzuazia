from aiogram import types
from aiogram.dispatcher.filters import Text, Command

from loader import dp, bot

@dp.message_handler(Text(equals=["Новости компаний"]))
@dp.message_handler(Command('news'))
async def bot_news(message: types.Message):
    text = message.text
    await message.answer(f"Ты попал на вкладку 'Новости', нажав команду {text}")
from aiogram import types
from aiogram.dispatcher.filters import Text, Command

from loader import dp, bot

@dp.message_handler(Text(equals=["Новости компаний"]))
@dp.message_handler(Command('news'))
async def bot_news(message: types.Message):
    text = message.text
    await message.answer(f"Воу-воу, мы только начали) Компании еще не успели ничего сделать")
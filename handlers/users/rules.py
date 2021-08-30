from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text

from loader import dp


@dp.message_handler(Text(equals=["Правила"]))
@dp.message_handler(Command('/rules'))
async def bot_rules(message: types.Message):
    text = ("Правила игры")
    await message.answer(text)
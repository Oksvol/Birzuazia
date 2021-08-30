from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text

from loader import dp


@dp.message_handler(Text(equals=["Связаться/подписаться"]))
@dp.message_handler(Command('/contacts'))
async def bot_contacts(message: types.Message):
    text = ("Создатель: @LeonardVaxberg")

    await message.answer(text)

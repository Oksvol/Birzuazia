from aiogram import types

from loader import dp, bot

@dp.message_handler(text='/lk')
async def bot_echo(message: types.Message):
    text = message.text
    await message.answer(f"Ты попал на вкладку 'Личный кабинет', нажав команду {text}")
from aiogram import types

from loader import dp, bot

@dp.message_handler(text='/portfel')
async def bot_echo(message: types.Message):
    text = message.text
    await message.answer(f"Ты попал на вкладку 'Портфель', нажав команду {text}")
from aiogram import types

from loader import dp, bot

@dp.message_handler(text='/lk')
async def bot_echo(message: types.Message):
    text = message.text
    full_name = message.from_user.full_name
    await message.answer(f"Имя: {full_name} \n"
                         f"Баланс: 8000000 \n")
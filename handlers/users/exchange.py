from aiogram import types

from loader import dp, bot

@dp.message_handler(text='/exchange')
async def bot_echo(message: types.Message):
    await message.answer(f"Биржа – это основной инструмент игры. \n"
                         f"Здесь ты можешь покупать ценные бумаги, чтобы обогатиться и раскачать капитал. \n")
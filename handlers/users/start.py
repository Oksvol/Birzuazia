import logging

from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from aiogram.dispatcher.filters.builtin import CommandStart


from filters.test_filter import SomeF
from loader import dp
from utils.misc import rate_limit


# Можно запускать раз в 10 сек
@rate_limit(limit=10)
@dp.message_handler(CommandHelp())
async def bothelp(message: types.Message):
    await message.answer("/block_me - Заблокироваться, /unblock_me - Разблокироваться")


#@rate_limit(5, key="start")
@dp.message_handler(CommandStart(), SomeF())
async def bot_start(message: types.Message, middleware_data, from_filter):
    await message.answer(f"Привет, {message.from_user.full_name}!\n\n" 
                         f"Добро пожаловать в страну Биржуазию, где все жители – инвесторы, а бизнес тусуется на бирже."
                         )


@dp.callback_query_handler(text="button")
async def get_button(call: types.CallbackQuery):
    await call.message.answer("Вы нажали на кнопку")

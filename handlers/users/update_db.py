from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hcode

from loader import dp
from utils.db_api import quick_commands as db


@dp.message_handler(Command("username"))
async def change_username(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой новый username")
    await state.set_state("username")


@dp.message_handler(state="username")
async def enter_username(message: types.Message, state: FSMContext):
    username = message.text
    await db.update_user_username(username=username, telegram_id=message.from_user.id)
    user = await db.select_user(telegram_id=message.from_user.id)
    user = dict(user)
    await message.answer("Данные обновлены. Запись в БД:\n" +
                         hcode(f"{user.id}"))
    await state.finish()
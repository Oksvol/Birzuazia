from aiogram import types
from aiogram.dispatcher.filters import Text, Command

from loader import dp, bot
from utils.db_api.quick_commands import select_user


@dp.message_handler(Text(equals=["Личный кабинет"]))
@dp.message_handler(Command('lk'))
async def bot_lk(message: types.Message):
    user = await select_user(int(message.from_user.id))
    full_name = message.from_user.full_name
    await message.answer(f"Имя: {full_name} \n"
                         f"Баланс: ${user.balance} \n")
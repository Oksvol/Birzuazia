
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from utils.db_api import quick_commands as db


from keyboards.default import start_menu


#@rate_limit(5, key="start")
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, ):
    await db.add_user(id=message.from_user.id,
                     full_name=message.from_user.full_name,
                     username=message.from_user.username,
                     balance=350000)

    user = await db.select_user(id=message.from_user.id)
    count = await db.count_users()

    # await message.answer(
    #     "\n".join(
    #         [
    #             f'Привет, {message.from_user.full_name}!',
    #             f'Ты был занесен в базу',
    #             f'В базе <b>{count}</b> пользователей\n\n',
    #             f'Твой баланс: ${user.balance}\n'
    #             "",
    #             f"<code>User: @{user.username} - {user.full_name}</code>",
    #         ]))

    await message.answer(f"Привет, {message.from_user.full_name}!\n\n" 
                         f"Добро пожаловать в страну Биржуазию, где все жители – инвесторы, а любой бизнес имеет свои акции на рынке."
                         "Цель каждого гражданина Биржуазии – наращивать капитал, поддерживая бизнес.\n\n"
                         "Сначала давай разберёмся в основах игры. Жми /help"
                         "\n\n"
                         # "Чтобы связаться с разработчиком или познакомиться с 'Забиржуазными' новостями, нажми /contacts\n\n"
                         "Приятной игры!", reply_markup=start_menu
                         )

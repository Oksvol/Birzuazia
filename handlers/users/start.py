from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp

from bot.keyboards.default import start_menu


#@rate_limit(5, key="start")
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, ):
    await message.answer(f"Привет, {message.from_user.full_name}!\n\n" 
                         f"Добро пожаловать в страну Биржуазию, где все жители – инвесторы, а любой бизнес имеет свои акции на рынке."
                         "Цель каждого гражданина Биржуазии – наращивать капитал, поддерживая бизнес.\n\n"
                         # "Если хочешь получше разобраться в игре нажми /help\n\n"
                         # "В игре есть немного правил, поэтому почитай их. Для этого нажми /rules\n\n"
                         # "Чтобы связаться с разработчиком или познакомиться с 'Забиржуазными' новостями, нажми /contacts\n\n"
                         "Приятной игры!", reply_markup=start_menu
                         )


@dp.message_handler(Text(equals=["Котлетки"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove())

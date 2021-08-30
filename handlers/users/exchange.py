

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text

from keyboards.inline.industries_buttons import industries

from loader import dp


@dp.message_handler(Text(equals=["Биржа"]))
@dp.message_handler(Command('exchange'))
async def bot_exchange(message: types.Message):
    await message.answer(f"Биржа – это основной инструмент игры. \n"
                         f"Здесь ты можешь покупать ценные бумаги, чтобы обогатиться и раскачать капитал. \n\n"
                         f"Все компании поделены по отраслям. \n\n"
                         f"Выбирай отрасль и внутри будет список компаний. Купить можно сколько угодно, но не больше, чем позволяет твой капитал.\n\n"
                         f"Если у тебя уже есть акции компании, то их можно продать по текущей цене.", reply_markup=industries
                         )
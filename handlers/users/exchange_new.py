
from aiogram.dispatcher.filters import Command
from aiogram import types

from keyboards.inline.exchange_btns import exchange_keyboard
from loader import dp


@dp.message_handler(Command("exchange_new"))
async def show_items(message: types.Message):
    markup = await exchange_keyboard()
    await message.answer(f"Биржа – это основной инструмент игры. \n"
                         f"Здесь ты можешь покупать ценные бумаги, чтобы обогатиться и раскачать капитал. \n\n"
                         f"Все компании поделены по отраслям. \n\n"
                         f"Выбирай отрасль и внутри будет список компаний. Купить можно сколько угодно, но не больше, чем позволяет твой капитал.\n\n"
                         f"Если у тебя уже есть акции компании, то их можно продать по текущей цене.",
                         reply_markup=markup)
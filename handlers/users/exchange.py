

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.types import CallbackQuery, message

from keyboards.inline.callback_datas import industries_callback
from keyboards.inline.industries_buttons import industries

from loader import dp, db


@dp.message_handler(Text(equals=["Биржа"]))
@dp.message_handler(Command('exchange'))
async def bot_exchange(message: types.Message):
    await message.answer(f"Биржа – это основной инструмент игры. \n"
                         f"Здесь ты можешь покупать ценные бумаги, чтобы обогатиться и раскачать капитал. \n\n"
                         f"Все компании поделены по отраслям. \n\n"
                         f"Выбирай отрасль и внутри будет список компаний. Купить можно сколько угодно, но не больше, чем позволяет твой капитал.\n\n"
                         f"Если у тебя уже есть акции компании, то их можно продать по текущей цене.", reply_markup=industries
                         )

# Попробуйем отловить по встроенному фильтру, где в нашем call.data содержится "industry"
@dp.callback_query_handler(industries_callback.filter(name="entertainment"))
async def buying_entertainment(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    name = callback_data.get("name")
    await call.message.answer(f"Вы выбрали {name}.")

# Попробуем использовать фильтр от CallbackData
@dp.inline_handler(industries_callback.filter(name="entertainment"))
async def show_entertainment(call: CallbackQuery, query: types.InlineQuery, callback_data: dict):
    await call.answer(cache_time=60)

    name = callback_data.get("name")
    await query.answer(switch_pm_parameter=name)
    try:
        shares = await db.select_shares(industry=name)
    except:
        pass

    shares_list = []

    for share in shares:
        shares_list.append(share.get("id"), share.get("tiker"), share.get("title"), share.get("description"), share.get("price"))
    for i in shares_list:
        await query.answer(
            results=[
                types.InlineQueryResultArticle(
                    id=i[0],
                    title=i[2],
                    input_message_content=types.InputTextMessageContent(
                        message_text="Тут какой-то <b>текст</b>, который будет отправлен при нажатии на кнопку",
                        parse_mode="HTML"
                    ),
                    url="https://core.telegram.org/bots/api#inlinequeryresult",
                    thumb_url="https://apps-cdn.athom.com/app/org.telegram.api.bot/1/1c9f8d07-be07-442d-933d-16fd212a68f1/assets/images/large.png",
                    description=i[2]
                ),
            ],
        )
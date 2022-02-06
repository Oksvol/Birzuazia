from datetime import datetime, date

from aiogram import types
from aiogram.dispatcher.filters import Text, Command

from loader import dp, bot
from utils.misc.list_news import global_news_list, exchange_news_list


@dp.message_handler(Text(equals=["Новости компаний"]))
@dp.message_handler(Command('news'))
async def bot_news(message: types.Message):
    date = '2022/1/15'
    dt = datetime.strptime(date, "%Y/%m/%d")

    global_news = await global_news_list(dt)
    string_global_news = "".join(global_news)
    exchange_news = await exchange_news_list(dt)
    string_exchange_news = "".join(exchange_news)



    text_exchange = f'<b>Биржевые новости:</b>\n\n' \
                    f'{string_exchange_news}'
    text_global = f'<b>Глобальные новости:</b>\n\n' \
                  f'{string_global_news}'
    text = f'<b>Биржевые новости:</b>\n\n' \
           f'{string_exchange_news}\n\n'\
           f'<b>Глобальные новости:</b>\n\n' \
           f'{string_global_news}'


    await message.answer(text)
    #await message.answer(text_exchange)
    #await message.answer(text_global)

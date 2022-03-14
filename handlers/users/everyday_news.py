from datetime import datetime, date

from data.config import ADMINS
import logging

from loader import dp, bot, scheduler
from utils.db_api.quick_commands import select_all_users
from utils.misc.list_news import global_news_list, exchange_news_list, exchange_news_list_and_change_price


async def everyday_news():
    users = await select_all_users()
    dt = date.today()
    await exchange_news_list_and_change_price(dt)
    for user in users:
        try:

            global_news = await global_news_list(dt)
            string_global_news = "".join(global_news)
            exchange_news = await exchange_news_list(dt)
            string_exchange_news = "".join(exchange_news)
            if string_exchange_news:
                text_exchange = f'<b>Биржевые новости:</b>\n\n' \
                                f'{string_exchange_news}'
                await dp.bot.send_message(user.id, text_exchange)
            if string_global_news:
                text_global = f'<b>Глобальные новости:</b>\n\n' \
                              f'{string_global_news}'
                await dp.bot.send_message(user.id, text_global)

        except Exception as err:
            text = f'Ошибика: {err} \n Пользователь: {user.id}'
            await dp.bot.send_message(112213378, text)

    for admin in ADMINS:
        check_message = 'Новости отправлены!'
        await dp.bot.send_message(admin, check_message)


def schedule_jobs():
    scheduler.add_job(everyday_news, "cron", day="*", hour="9", minute="10")

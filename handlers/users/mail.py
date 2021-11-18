import logging

from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command
from loader import dp

from data.config import ADMINS
from utils.db_api.quick_commands import select_all_users


@dp.message_handler(Command('mail'))
async def on_startup_notify(dp: Dispatcher):
    users = await select_all_users()
    user_ids = []
    for user in users:
        user_ids.append(user.id)

    for user in user_ids:
        try:
            await dp.bot.send_message(user, "Privyau! Это тестовая рассылка, а заодно и небольшое сообщение) Все операции будут удалены, активы из ваших портфелей пропадут и состояние счетов вернется в базовое состояние) Готовим бота к второму этапу. Не скучайте;)")

        except Exception as err:
            logging.exception(err)
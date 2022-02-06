from loader import dp, scheduler
from data.config import ADMINS
import logging


async def scheduled_messages():
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Привет! Это тестовое сообщение")

        except Exception as err:
            logging.exception(err)

def schedule_jobs():
    scheduler.add_job(scheduled_messages, "cron", day="*", hour="15", minute="00")


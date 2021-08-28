from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot

@dp.message_handler(Command('menu'))
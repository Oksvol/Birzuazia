from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Документация по текстовым кнопкам: https://core.telegram.org/bots/api#replykeyboardmarkup

cancel_operation = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отмена"),
        ]
    ],
    resize_keyboard=True
)
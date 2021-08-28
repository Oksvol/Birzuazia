from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Документация по текстовым кнопкам: https://core.telegram.org/bots/api#replykeyboardmarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Котлетки"),
        ],
        [
            KeyboardButton(text="Макарошки"),
            KeyboardButton(text="Пюрешка")
        ],
    ],
    resize_keyboard=True
)
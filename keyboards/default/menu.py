from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Документация по текстовым кнопкам: https://core.telegram.org/bots/api#replykeyboardmarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Биржа"),
        ],
        [
            KeyboardButton(text="Новости компаний")
        ],
        [
            KeyboardButton(text="Состояние счета")
        ],
        [
            KeyboardButton(text="Личный кабинет")
        ],
    ],
    resize_keyboard=True
)
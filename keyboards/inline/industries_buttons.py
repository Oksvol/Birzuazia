from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import industries_callback


# Вариант 2 - с помощью row_width и insert.
industries = InlineKeyboardMarkup(row_width=1)

entertainment = InlineKeyboardButton(text="Развлечения", callback_data=industries_callback.new(name="Развлечения", quantity="1"))
industries.insert(entertainment)

industry = InlineKeyboardButton(text="Промышленность", callback_data=industries_callback.new(name="Промышленность", quantity="1"))
industries.insert(industry)

agro_industry = InlineKeyboardButton(text="Аграрная промышленность", callback_data=industries_callback.new(name="Аграрная промышленность", quantity="1"))
industries.insert(agro_industry)

war_industry = InlineKeyboardButton(text="Военная промышленность", callback_data=industries_callback.new(name="Военная промышленность", quantity="1"))
industries.insert(war_industry)

law = InlineKeyboardButton(text="Юриспруденция", callback_data=industries_callback.new(name="Юриспруденция", quantity="1"))
industries.insert(law)

resources = InlineKeyboardButton(text="Добыча ресурсов", callback_data=industries_callback.new(name="Добыча ресурсов", quantity="1"))
industries.insert(resources)

jewelry = InlineKeyboardButton(text="Ювелирное дело", callback_data=industries_callback.new(name="Ювелирное дело", quantity="1"))
industries.insert(jewelry)

cars = InlineKeyboardButton(text="Автомобилестроение", callback_data=industries_callback.new(name="Автомобилестроение", quantity="1"))
industries.insert(cars)

farma = InlineKeyboardButton(text="Фармацевтика", callback_data=industries_callback.new(name="Фармацевтика", quantity="1"))
industries.insert(farma)

medicine = InlineKeyboardButton(text="Медицина", callback_data=industries_callback.new(name="Медицина", quantity="1"))
industries.insert(medicine)

it = InlineKeyboardButton(text="IT", callback_data=industries_callback.new(name="IT", quantity="1"))
industries.insert(it)

merchant = InlineKeyboardButton(text="Торговля", callback_data=industries_callback.new(name="Торговля", quantity="1"))
industries.insert(merchant)

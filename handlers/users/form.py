from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Command
from loader import dp

from states.forms import Form


@dp.message_handler(Command('form'))
async def enter_form(message: types.Message):
    await message.answer("Давайте познакомимся!\n\n"
                         "Как вас зовут?")
    await Form.name.set()

@dp.message_handler(state=Form.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text

    async with state.proxy() as data:
        data["name"] = name
        # Удобно, если нужно сделать data["some_digit"] += 1
        # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать

    await message.answer("Укажите ваш Email")

    await Form.email.set()

@dp.message_handler(state=Form.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    async with state.proxy() as data:
        data["email"] = email
        # Удобно, если нужно сделать data["some_digit"] += 1
        # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать

    await message.answer("Куда можно позвонить?")

    await Form.next()

@dp.message_handler(state=Form.phone)
async def answer_email(message: types.Message, state: FSMContext):

    # Достаем переменные
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = message.text

    await message.answer("Привет! Ты ввел следующие данные:\n\n"
                         f"Имя: {name}\n\n"
                         f"Email: {email}\n\n"
                         f"Телефон: {phone}")

    # Вариант 1
    await state.finish()

    # Вариант завершения 2
    # await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    # await state.reset_state(with_data=False)
from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Command
from loader import dp

from states.test import Test


@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование. \n\n"
                         "Вопрос №1. \n\n"
                         "Вы часто играете в компьютер?")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    # Вариант 2 получения state
    # state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    # Вариант 1 сохранения переменных - записываем через key=var
    # Если у вас запись идет какого-то параметра (например email) то записывайте не answer,
    # а email, чтобы потом было понятно что именно доставать
    # await state.update_data(answer1=answer)

    # Вариант 2 - передаем как словарь
    # await state.update_data(
    #     {"answer1": answer}
    # )

    # Вариант 3 - через state.proxy
    async with state.proxy() as data:
        data["answer1"] = answer
        # Удобно, если нужно сделать data["some_digit"] += 1
        # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать

    await message.answer("Вопрос №2. \n\n"
                         "Ваша память ухудшилась и вы помните то, что было давно, но забываете недавние события?")

    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    # Достаем переменные
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ваши ответы!")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

    # Вариант 1
    await state.finish()

    # Вариант завершения 2
    # await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    # await state.reset_state(with_data=False)
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

from data.config import allowed_users


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать при этом на кнопку",
                    parse_mode="HTML"
                ),
            ),
        ],

        cache_time=5)

# @dp.inline_handler()
# async def empty_query(query: types.InlineQuery):
#     user = query.from_user.id
#     if user not in allowed_users:
#         await query.answer(
#             results=[],
#             switch_pm_text="Бот недоступен. Подключить бота",
#             switch_pm_parameter="connect_user",
#             cache_time=5)
#         return
#     await query.answer(
#         results=[
#             types.InlineQueryResultArticle(
#                 id="1",
#                 title="Название, которое отображается в инлайн режиме!",
#                 input_message_content=types.InputTextMessageContent(
#                     message_text="Тут какой-то <b>текст</b>, который будет отправлен при нажатии на кнопку",
#                     parse_mode="HTML"
#                 ),
#                 url="https://core.telegram.org/bots/api#inlinequeryresult",
#                 thumb_url="https://apps-cdn.athom.com/app/org.telegram.api.bot/1/1c9f8d07-be07-442d-933d-16fd212a68f1/assets/images/large.png",
#                 description="Описание, в инлнайн режиме"
#             ),
#             # types.InlineQueryResultCachedPhoto(
#             #     id="2",
#             #     photo_file_id="AgACAgIAAxkBAAICcV6jF5kAARvDMn99PQuVe9fBg-TKcAACQ64xG0WQGEm4F3v9dsbAAg7Hwg8ABAEAAwIAA3kAA9c_BgABGQQ",
#             #     description="Описание, которое нигде не отображается!",
#             #     caption="Тут будет подпись, которая отправится с картинкой, если на нее нажать",
#             # ),
#             types.InlineQueryResultVideo(
#                 id="4",
#                 video_url="https://pixabay.com/en/videos/download/video-10737_medium.mp4",
#                 caption="Подпись к видео",
#                 description="Какое-то описание",
#                 title="Название видео",
#                 thumb_url="https://i0.wp.com/globaldiversitypractice.com/wp-content/uploads/2018/11/asda.jpg",
#                 mime_type="video/mp4",  # Или video/mp4 text/html
#             ),
#         ],
#     )
#
# @dp.message_handler(CommandStart(deep_link="connect_user"))
# async def connect_user(message: types.Message):
#     allowed_users.append(message.from_user.id)
#     await message.answer("Вы подключены",
#                          reply_markup=InlineKeyboardMarkup(
#                              inline_keyboard=[
#                                  [
#                                      InlineKeyboardButton(text="Войти в инлайн режим",
#                                                           switch_inline_query_current_chat="Запрос")
#                                  ]
#                              ]
#                          )
#                          )

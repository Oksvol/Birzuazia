import logging

from aiogram import types
from aiogram.dispatcher.filters import Text, Command

from loader import dp, bot
from utils.db_api.quick_commands import select_user, select_all_users
from utils.misc.count_balance import show_balance, show_user_portfel, get_user_portfel
from utils.misc.prettifying import money_format


@dp.message_handler(Command('stats'))
async def bot_portfel(message: types.Message):
    users = await select_all_users()
    for user in users:
        try:
            balance = await show_balance(user.id)
            show_portfel = await show_user_portfel(user.id)
            string_portfel = "".join(show_portfel)
            portfel_data = await get_user_portfel(user.id)
            sum_assets = 0
            for asset in portfel_data:
                sum_assets += float(asset[2])
            profit = float((float(balance) + sum_assets - float(user.balance))/float(user.balance)*100)
            total_sum_portfel = float(balance) + sum_assets
            profit = round(profit, 3)

            if profit > 0:
                profit_info = '<b>Прибыль за весь период: </b>' + "🟢 " + str(profit) + '% \n\n'
            elif profit < 0:
                profit_info = '<b>Прибыль за весь период: </b>' + "🔴 " + str(profit) + '% \n\n'
            elif profit == 0:
                profit_info = '<b>Прибыль за весь период: </b>' + "⚪️ " + str(profit) + '% \n\n'

            text = f'<b>Пользователь:</b> {user.id}, {user.full_name}  \n\n' \
                   f'<b>Баланс:</b> ${await money_format(total_sum_portfel)} \n\n' \
                   f'<b>Сумма активов:</b> ${await money_format(sum_assets)} \n\n' \
                   f'<b>Свободные деньги:</b> ${await money_format(balance)} \n\n' \
                   f'{profit_info}' \
                   f'<b>Активы:</b> \n\n' \
                   f'{string_portfel}'

            await dp.bot.send_message(112213378, text)

        except Exception as err:
            text = f'Ошибика: {err} \n Пользователь: {user}'
            await dp.bot.send_message(112213378, text)

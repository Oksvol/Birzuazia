from utils.db_api.quick_commands import get_operations_of_user_by_tiker


async def count_operations_by_tiker(user, tiker):
    user_operations = await get_operations_of_user_by_tiker(user, tiker)
    buys = 0
    sells = 0

    for op in user_operations:
        if op.type == 'buy':
            buys += op.quantity
        elif op.type == 'sell':
            sells += op.quantity

    balance_share = buys - sells
    return balance_share

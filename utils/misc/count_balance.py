from utils.db_api.quick_commands import select_user, get_operations_of_user


async def show_balance(user):
    player = await select_user(int(user))
    operations = await get_operations_of_user(user)

    buys = 0
    sells = 0
    for op in operations:
        if op.type == 'buy':
            buys += op.price * op.quantity
        if op.type == 'sell':
            sells += op.price * op.quantity

    balance = player.balance - buys + sells

    return balance


async def show_shares_of_user(user):
    player = await select_user(int(user))
    operations = await get_operations_of_user(user)

    buys = 0
    sells = 0
    for op in operations:
        if op.type == 'buy':
            buys += op.price * op.quantity
        if op.type == 'sell':
            sells += op.price * op.quantity

    balance = player.balance - buys + sells

    return balance
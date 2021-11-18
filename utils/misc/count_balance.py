from utils.db_api.quick_commands import select_user, get_operations_of_user, get_share
from utils.misc.count_share_balance import count_operations_by_tiker
from utils.misc.prettifying import money_format, grades_format


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



async def show_user_portfel(user):
    operations = await get_operations_of_user(user)

    tikers = []
    portfel = []

    for op in operations:
        if op.tiker not in tikers:
            tikers.append(op.tiker)

    portfel.append("Тикер : Количество : Текущая стоимость \n\n")

    for tik in tikers:
        quantity = await count_operations_by_tiker(user, tik)
        tiker = tik
        share = await get_share(tik)
        sum = quantity * share.price
        # asset = (tiker, quantity, sum)
        # portfel.append(asset)
        # portfel.append('\n')
        if quantity > 0:
            portfel.append('<b>')
            portfel.append(tiker)
            portfel.append('</b>')
            portfel.append(" : ")
            portfel.append(await grades_format(quantity))
            portfel.append(" шт. :  $")
            portfel.append(await money_format(sum))
            portfel.append("\n")

    return portfel


async def get_user_portfel(user):
    operations = await get_operations_of_user(user)

    tikers = []
    portfel = []

    for op in operations:
        if op.tiker not in tikers:
            tikers.append(op.tiker)

    for tik in tikers:
        quantity = await count_operations_by_tiker(user, tik)
        tiker = tik
        share = await get_share(tik)
        sum = quantity * share.price
        asset = (tiker, quantity, float(sum))
        portfel.append(asset)

    return portfel
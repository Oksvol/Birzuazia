from utils.db_api.quick_commands import select_news_global_by_date, select_all_news_global, \
    select_news_exchange_by_date, get_share, update_share_price


async def global_news_list(dt):
    global_news = await select_news_global_by_date(dt)

    global_news_list = []

    for n in global_news:
        global_news_list.append('<b>')
        global_news_list.append(n.tiker)
        global_news_list.append('</b>')
        global_news_list.append("\n")
        global_news_list.append(n.text)
        global_news_list.append("\n")
        global_news_list.append("\n")

    return global_news_list


async def exchange_news_list(dt):
    exchange_news = await select_news_exchange_by_date(dt)

    exchange_news_list = []

    for n in exchange_news:
        exchange_news_list.append('<b>')
        exchange_news_list.append(n.tiker)
        exchange_news_list.append('</b>')
        exchange_news_list.append("\n")
        exchange_news_list.append(n.text)
        exchange_news_list.append("\n")
        exchange_news_list.append("\n")

    return exchange_news_list


async def exchange_news_list_and_change_price(dt):
    exchange_news = await select_news_exchange_by_date(dt)

    for n in exchange_news:
        tiker = n.tiker
        share = await get_share(tiker)
        price = share.price + (share.price * n.change) # обновить цену с учетом изменения цены
        await update_share_price(tiker, price)

    news_list = await exchange_news_list(dt)

    return news_list


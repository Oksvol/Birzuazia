import random

from utils.db_api.quick_commands import select_all_shares, update_share_price


async def rand_prices():
    shares = await select_all_shares()
    for share in shares:
        price = int(share.price)
        if price < 5:
            share_price = random.uniform(price + (price / 100 * 1), price + (price / 100 * 2))
        else:
            share_price = random.uniform(price - (price / 100 * 2), price + (price / 100 * 2))
        await update_share_price(share.tiker, share_price)

    return


if __name__ == '__main__':
    rand_prices()
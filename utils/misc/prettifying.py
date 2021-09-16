

async def money_format(value):
    pretty_value = '{0:,}'.format(value).replace(',', ' ').replace('.', ',')

    return pretty_value
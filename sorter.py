def sort(price_list, volume_list):
    """Ordena de menor a mayor la lista de precios con su volumen de ventas"""

    prices = len(price_list)

    for i in range(prices):
        for k in range(prices):

            try:
                price1 = float(price_list[i][5:])
            except:
                price1 = float(price_list[i])

            try:
                price2 = float(price_list[k][5:])
            except:
                price2 = float(price_list[k])

            if price1 < price2:

                price_list[i], price_list[k] = price_list[k], price_list[i]
                volume_list[i], volume_list[k] = volume_list[k], volume_list[i]

    for i in range(len(volume_list)):
        volume_list[i] = int(volume_list[i].replace(",", ""))

    return price_list, volume_list


def sort_profit(apps):

    cheap_list = []
    average_list = []
    noprofit = []

    for app_id in apps:
        (
            game_name,
            game_price,
            cards_drop,
            price_cards,
            average,
            cheap_card,
            cheap_profit,
            average_profit,
            sale_alert,
            expensive_alert,
        ) = apps[app_id]

        try:
            if cheap_card - game_price > 0:
                cheap_list.append(app_id)

            elif average - game_price > 0:
                average_list.append(app_id)

            else:
                noprofit.append(app_id)

        except:
            pass

    return cheap_list, average_list, noprofit

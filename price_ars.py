import math
from prices_list import prices_list

def price_ars (app_id, games_to_scan, scanned_games):

    price_list, volume_list, cards, success, game_name = prices_list(app_id, games_to_scan, scanned_games)

    price_cards = 0
    cards_drop = math.ceil(cards/2)

    if success == True:

        for price in price_list:

            price_cards += float(price.replace('ARS$ ',''))

        price_cards = round(price_cards,2)


    return price_cards, cards_drop, cards, price_list, volume_list, success, game_name
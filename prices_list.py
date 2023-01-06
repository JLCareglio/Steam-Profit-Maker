import json
import os
import time
import urllib.parse

import requests
from bs4 import BeautifulSoup
from colorama import Back, Fore, Style, init
from dotenv import load_dotenv

from get_hash import get_market_hash


def prices_list(app_id, games_to_scan, scanned_games):

    loaded_cards = 1

    API_URL = os.getenv("API_ENDPOINT_URL")
    AUTH_KEY = os.getenv("PROXIESAPI_AUTH_KEY")

    try:
        market_hash, cards, game_name = get_market_hash(
            app_id, scanned_games, games_to_scan
        )

    except:
        market_hash = []
        cards = 0
        game_name = None

    prices = []
    volume_list = []
    success = True

    for card_hash in market_hash:
        datos = None
        url = "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name=" + urllib.parse.quote(
            card_hash
        ).replace(
            "/", "-"
        )

        if AUTH_KEY == None:
            datos = requests.get(url).content
        else:
            PARAMS = {"auth_key": AUTH_KEY, "url": url}
            datos = requests.get(url=API_URL, params=PARAMS).content

        soup = BeautifulSoup(datos, features="html.parser")
        card_json = json.loads(str(soup))

        points = "." * (loaded_cards % 4)

        os.system("cls")
        loading_text = Fore.CYAN + "Cargando: {} cartas de {}{}".format(
            loaded_cards, cards, points
        )
        loading_bar = (
            Fore.YELLOW
            + Style.DIM
            + "─   [ "
            + Fore.WHITE
            + str("- " * cards).replace(
                "-", Fore.GREEN + "■" + Fore.WHITE, loaded_cards
            )
            + Fore.YELLOW
            + "]   ─"
            + Fore.WHITE
        )

        print(
            Style.BRIGHT
            + "App ID: "
            + str(app_id)
            + "  ─  "
            + "Juego {} de {}\n".format(scanned_games, games_to_scan)
        )
        print(loading_text)
        print(loading_bar)

        loaded_cards += 1
        time.sleep(2.5)

        try:
            success = card_json["success"]
        except:
            print("Problema con el cromo")
            pass

        if success == True:

            try:
                price_card = card_json["lowest_price"]
            except:
                price_card = "0"
                print("Problema con el lowest_price")

            try:
                volume = card_json["volume"]
            except:
                volume = "0"
                # print('Problema con el Volumen')

            prices += (price_card.replace(".", "").replace(",", "."),)
            volume_list += (volume,)

        else:
            try:
                url += "%20%28Trading%20Card%29"
                datos = requests.get(url).content
                soup = BeautifulSoup(datos, features="html.parser")
                card_json = json.loads(str(soup))

                price_card = card_json["lowest_price"]
                success = card_json["success"]

                try:
                    volume = card_json["volume"]
                except:
                    volume = "0"

                prices += (price_card.replace(",", "."),)
                volume_list += (volume,)

            except:
                volume = "0"
                price_card = "0"
                success = False

                break

    if len(market_hash) == 0:
        volume = "0"
        price_card = "0"
        prices = []
        volume_list = []
        cards = 0
        success = False

    return prices, volume_list, cards, success, game_name

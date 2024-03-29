import json
import os
import time
import urllib.parse

import requests
from bs4 import BeautifulSoup
from colorama import Back, Fore, Style, init

from get_hash import get_market_hash


def prices_list(app_id, games_to_scan, scanned_games):
    loaded_cards = 1

    # API_URL = "http://api.proxiesapi.com"
    LINE_UP = "\033[1A"
    LINE_CLEAR = "\x1b[2K"

    try:
        market_hash, cards, game_name = get_market_hash(
            app_id, scanned_games, games_to_scan
        )
    except Exception as e:
        print(e)
        # input("pulse enter para continuar")
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

        # if not api_key:
        #     datos = requests.get(url).content
        # else:
        #     PARAMS = {"auth_key": api_key, "url": url}
        #     datos = requests.get(url=API_URL, params=PARAMS).content

        datos = requests.get(url).content

        soup = BeautifulSoup(datos, features="html.parser")
        card_json = json.loads(str(soup))

        points = "." * (loaded_cards % 4)
        card_name = card_hash.split("-", 1)[1]
        # proxy_text = "🕵️" if api_key else ""

        for i in range(5):
            print(LINE_UP, end=LINE_CLEAR)
        cant_line_clear = 0

        loading_text = f"{Fore.CYAN}Cargando 🎴: {loaded_cards} de {cards} ({card_name}){points}"

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
            + f"🎮 {game_name}\n👀 Juego {scanned_games} de {games_to_scan}  ─  🔑 AppID: {str(app_id)}\n"
        )
        print(loading_text)
        print(loading_bar)

        loaded_cards += 1
        time.sleep(2.5)

        try:
            success = card_json["success"]
            try:
                price_card = card_json["lowest_price"]
            except:
                price_card = "0"
                # print("Problema con el lowest_price en: " + url)
                # cant_line_clear += 1
                # time.sleep(1)
                success = False

            try:
                volume = card_json["volume"]
            except:
                volume = "0"
                # print("Problema con el Volumen en: " + url)
                # cant_line_clear += 1
                # time.sleep(1)
                success = False
        except:
            # print("Problema con el cromo en: " + url)
            # cant_line_clear += 1
            # time.sleep(1)
            success = False
            pass

        if success:
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

        for i in range(cant_line_clear):
            print(LINE_UP, end=LINE_CLEAR)

    if len(market_hash) == 0:
        volume = "0"
        price_card = "0"
        prices = []
        volume_list = []
        cards = 0
        success = False

    return prices, volume_list, cards, success, game_name

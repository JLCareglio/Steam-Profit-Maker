import os

import requests
from bs4 import BeautifulSoup


def get_market_hash(app_id, scanned_games, games_to_scan):

    url = "https://www.steamcardexchange.net/index.php?gamepage-appid-" + str(app_id)
    datos = requests.get(url).content
    soup = BeautifulSoup(datos, features="html.parser")
    market_hash = []

    try:
        game_name = soup.select_one(
            "body > main > div.flex.items-center.px-2.py-3.mx-auto.mt-0\\.5.overflow-hidden.leading-tight.bg-black > span"
        ).text

        # game_name = soup.find("img", attrs={"class": "game-image"})["alt"]
        trading_cards = int(
            soup.select_one(
                "body > main > div.hidden.lg\\:grid.lg\\:grid-cols-4.\\32 xl\\:grid-cols-6.gap-0\\.5.mt-0\\.5.text-center > div:nth-child(1) > div > span"
            ).text
        )
        # trading_cards = int(soup.find("table", attrs={"class": "game-stats"}).th.text)
        cards_container = soup.select_one("body > main > div:nth-child(10)")
        cards_names = cards_container.select(".text-sm.text-center.break-words")
        # card_images = soup.find_all("img", attrs={"class": "element-image"}, limit=trading_cards)
    except Exception as e:
        os.system("clear")
        print(">>>> INICIO ERROR: >>>>")
        print(e)
        input("<<<< FIN ERROR <<<<")
    # os.system('clear')
    loaded_cards = 0
    loading_text = "Cargando 🎴: {} de {}".format(loaded_cards, trading_cards)

    loading_bar = (
        "─   [ " + str("- " * trading_cards).replace("-", "■", loaded_cards) + "]   ─"
    )

    print(
        "🎮 {}  ─  🔑 AppID: {}  ─  👀 Juego {} de {}\n".format(
            game_name, str(app_id), scanned_games, games_to_scan
        )
    )

    print(loading_text)
    print(loading_bar)

    for card_name in cards_names:
        market_hash += (str(app_id) + "-" + card_name.text,)
        # if card_name.has_attr("alt"):
        #   market_hash += (str(app_id) + "-" + card_name["alt"],)

    return market_hash, trading_cards, game_name

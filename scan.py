import os
import time

from colorama import Back, Fore, Style, init

import summary
from alerts import check
from price_ars import price_ars
from price_game import price_game
from sorter import sort
from summary import single

# 	Variables Globales
LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"


def single_scan(app_id):

    os.system("clear")
    print("⏳ Espere un momento...", end="\r")
    (
        price_total,
        cards_drop,
        cards_total,
        price_list,
        volume_list,
        success,
        game_name,
    ) = price_ars(app_id, 1, 1)

    if success == True:

        fees = 0.874
        expensive_alert = ""
        price_cards = "|| "

        price_list, volume_list = sort(price_list, volume_list)
        expensive_cards, sale_alert = check(price_list, volume_list)

        if expensive_cards > 0:

            for i in range(1, expensive_cards + 1):

                price_total -= float(price_list[-i][5:])

            expensive_alert = (
                "\n"
                + Fore.RED
                + ">ALERTA: El juego posee uno o mas cromos muy caros que no se venden."
                + Fore.WHITE
            )

        average = round(
            cards_drop * (float(price_total) / float(cards_total)) * fees, 2
        )

        cheap_card = round(float(price_list[0][5:]) * cards_drop * fees, 2)
        cheap_profit = "Profit con el cromo mas barato: No calculado"
        average_profit = "Profit promedio: No calculado"

        for i in range(len(price_list)):
            price_cards += str(price_list[i]) + ", " + str(volume_list[i]) + " || "

        game_price = price_game(app_id, game_name)
        cheap_profit = (
            "Profit con el cromo mas barato: "
            + "%.2f" % (cheap_card - game_price)
            + " ARS$"
        )

        if cheap_card - game_price > 0:
            cheap_profit = Fore.GREEN + cheap_profit + Fore.WHITE
        else:
            cheap_profit = Fore.RED + cheap_profit + Fore.WHITE

        if average - game_price > 0:
            average_profit = (
                Fore.GREEN
                + "Profit promedio: {} ARS$".format("%.2f" % (average - game_price))
                + Fore.WHITE
            )
        else:
            average_profit = (
                Fore.RED
                + "Profit promedio: {} ARS$".format("%.2f" % (average - game_price))
                + Fore.WHITE
            )

        app_data = {
            app_id: (
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
            )
        }
        summary = [
            app_id,
            game_name,
            game_price,
            cards_drop,
            price_cards,
            average,
            cheap_card,
            sale_alert,
            expensive_alert,
        ]

        os.system("clear")
        single(summary)

    else:
        print(
            "\nEl ID {} no tiene cromos/no existe en SteamCardExchange o genero algun error, introduzca otro.".format(
                app_id
            )
        )
        app_data = {}

    return app_data


def multi_scan(apps):

    bad_app_id = []
    app_data = {}
    scanned_games = 1

    os.system("clear")
    print("⏳ Espere un momento...", end="\r")

    for app_id in apps:

        (
            price_total,
            cards_drop,
            cards_total,
            price_list,
            volume_list,
            success,
            game_name,
        ) = price_ars(app_id, len(apps), scanned_games)

        for i in range(4):
            print(LINE_UP, end=LINE_CLEAR)

        scanned_games += 1

        if success == True:

            fees = 0.874
            expensive_alert = ""
            price_cards = "|| "

            price_list, volume_list = sort(price_list, volume_list)
            expensive_cards, sale_alert = check(price_list, volume_list)

            if expensive_cards > 0:

                for i in range(1, expensive_cards + 1):

                    price_total -= float(price_list[-i][5:])

                expensive_alert = (
                    "\n"
                    + Fore.RED
                    + ">ALERTA: El juego posee uno o mas cromos muy caros que no se venden."
                    + Fore.WHITE
                )

            average = round(cards_drop * (price_total / cards_total) * fees, 2)

            cheap_card = round(float(price_list[0][5:]) * cards_drop * fees, 2)
            cheap_profit = "Profit con el cromo mas barato: No calculado"
            average_profit = "Profit promedio: No calculado"

            for i in range(len(price_list)):
                price_cards += str(price_list[i]) + ", " + str(volume_list[i]) + " || "

            game_price = price_game(app_id, game_name)
            cheap_profit = (
                "Profit con el cromo mas barato: "
                + "%.2f" % (cheap_card - game_price)
                + " ARS$"
            )

            if cheap_card - game_price > 0:
                cheap_profit = Fore.GREEN + cheap_profit + Fore.WHITE
            else:
                cheap_profit = Fore.RED + cheap_profit + Fore.WHITE

            if average - game_price > 0:
                average_profit = (
                    Fore.GREEN
                    + "Profit promedio: {} ARS$".format("%.2f" % (average - game_price))
                    + Fore.WHITE
                )
            else:
                average_profit = (
                    Fore.RED
                    + "Profit promedio: {} ARS$".format("%.2f" % (average - game_price))
                    + Fore.WHITE
                )

            app_data[app_id] = (
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
            )

            summary = [
                app_id,
                game_name,
                game_price,
                cards_drop,
                price_cards,
                average,
                cheap_card,
                sale_alert,
                expensive_alert,
            ]

            single(summary)
            print(
                Fore.MAGENTA
                + "\n─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\n"
            )

        else:
            bad_app_id += (app_id,)
            app_data[app_id] = (None, 0, 0, 0, 0, 0, 0, 0, "", "")

    if len(bad_app_id) > 0:

        bad_id_string = ""

        for app_id in bad_app_id:
            bad_id_string += str(app_id) + " "

        print(
            Fore.RED
            + "Problemas con los siguientes App ID: {}\n".format(bad_id_string)
            + Fore.WHITE
        )

    return app_data

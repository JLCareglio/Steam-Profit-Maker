import os

from colorama import *

init()

LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"


def single(summary):

    (
        app_id,
        game_name,
        game_price,
        cards_drop,
        price_cards,
        average,
        cheap_card,
        sale_alert,
        expensive_alert,
    ) = summary

    fees = 0.874
    low_price_card = float(
        price_cards.replace(",", " ||").split("||")[1].lstrip(" ARS$").strip()
    )
    high_price_card = float(
        price_cards.replace(",", " ||").split("||")[-3].lstrip(" ARS$").strip()
    )
    cheap_card = round(low_price_card * cards_drop * fees, 2)
    expensive_card = round(high_price_card * cards_drop * fees, 2)

    try:
        cheap_profit = cheap_card - game_price
        expensive_profit = expensive_card - game_price
        average_profit = average - game_price

        cheap_profit = (
            Fore.GREEN + "%.2f" % (cheap_profit)
            if cheap_profit > 0
            else Fore.RED + "%.2f" % (cheap_profit)
        )

        expensive_profit = (
            Fore.GREEN + "%.2f" % (expensive_profit)
            if expensive_profit > 0
            else Fore.RED + "%.2f" % (expensive_profit)
        )

        average_profit = (
            Fore.GREEN + "%.2f" % (average_profit)
            if average_profit > 0
            else Fore.RED + "%.2f" % (average_profit)
        )

    except:
        cheap_profit = None
        average_profit = None

    print(Style.BRIGHT + Fore.BLUE + f"🎮 {game_name}  ─  🔑 AppID: {app_id}")
    print(
        Fore.BLUE
        + "🪙 Precio: {} $ARS  ─  🎴 Cromos obtenibles: {}".format(game_price, cards_drop)
        + Fore.WHITE
    )
    print(Style.DIM + "{}{}".format(sale_alert, expensive_alert) + Style.RESET_ALL)

    print(
        Fore.CYAN
        + "\n🎴 + Barato: {} $ARS	─  🎴 + Caro: {} $ARS".format(
            "%.2f" % (low_price_card), "%.2f" % (high_price_card)
        )
        + Fore.WHITE
    )
    # print(
    #     Fore.CYAN
    #     + "Promedio: {} $ARS	─  Con el cromo barato: {} $ARS".format(
    #         average, cheap_card
    #     )
    #     + Fore.WHITE
    # )

    if type(game_price) == float:
        print(
            f"""↘️ Profit mínimo posible: {cheap_profit} $ARS{Fore.WHITE}
↗️ Profit máximo posible: {expensive_profit} $ARS{Fore.WHITE}
➡️ Profit Promedio: {average_profit} $ARS{Fore.WHITE}"""
        )

    print("\n📝 Precio de todos los cromos y su volumen de ventas:\n" + price_cards)

    return 0


def multi(app_ids, cheap_list, average_list, noprofit):

    os.system("clear")

    if len(cheap_list) + len(average_list) != 0:

        if len(cheap_list) > 0:
            print(
                f"""        {Fore.GREEN}= = = = = = = = = = = = = = = = = = = = = = =
        ✅ Los siguientes {len(cheap_list)} juegos dan profit seguro:
        = = = = = = = = = = = = = = = = = = = = = = =\n"""
            )

            for app_id in cheap_list:
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
                ) = app_ids[app_id]

                summary = (
                    app_id,
                    game_name,
                    game_price,
                    cards_drop,
                    price_cards,
                    average,
                    cheap_card,
                    sale_alert,
                    expensive_alert,
                )

                single(summary)

                print(
                    Fore.MAGENTA
                    + "\n─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\n"
                )  # 30
            for i in range(2):
                print(LINE_UP, end=LINE_CLEAR)

        if len(average_list) > 0:
            print(
                f"""        {Fore.YELLOW}= = = = = = = = = = = = = = = = = = = = = = =
        👀 Los siguientes {len(average_list)} juegos pueden dar profit:
        = = = = = = = = = = = = = = = = = = = = = = =\n"""
            )

            for app_id in average_list:
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
                ) = app_ids[app_id]

                summary = (
                    app_id,
                    game_name,
                    game_price,
                    cards_drop,
                    price_cards,
                    average,
                    cheap_card,
                    sale_alert,
                    expensive_alert,
                )

                single(summary)
                print(
                    Fore.MAGENTA
                    + "\n─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\n"
                )  # 30
            for i in range(2):
                print(LINE_UP, end=LINE_CLEAR)

        if len(noprofit) > 0:
            print(
                f"""        {Fore.RED}= = = = = = = = = = = = = = = = = = = = = = =
        ⛔ Los siguientes {len(noprofit)} juegos no dan profit:
        = = = = = = = = = = = = = = = = = = = = = = ={Fore.WHITE}\n"""
            )

            for app_id in noprofit:
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
                ) = app_ids[app_id]

                print(f"🔑 AppID: {app_id}  ─  🎮 {game_name}")
            print(f"{Fore.WHITE}")

        print(
            f"{Fore.BLUE}Nota: se guardo un informe con todos los datos de los juegos escaneados.\nPuedes encontrar el informe dentro de la carpeta data en un archivo .csv con la fecha actual\n"
        )

    else:
        print("⛔ Ningún juego de la lista da profit.")

    app_ids_error = [k for k, v in app_ids.items() if v[0] == None]
    if len(app_ids_error) > 0:
        print(
            f"""{Fore.RED}
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
💥 Los siguientes {len(app_ids_error)} juegos no pudieron escanearse por un error critico:{Fore.YELLOW}
"""
        )
        for app_id in app_ids_error:
            print(app_id, end=" ")
        print("\n")


# sale_alert = Fore.RED + '	ALERTA: Los cromos se venden muy poco (menos de 10 ventas en las ultimas 24 hs)' + Fore.WHITE
# expensive_alert = '\n        ' + Fore.RED + 'ALERTA: El juego posee uno o mas cromos muy caros que no se venden.' + Fore.WHITE

# summary = (302490, 'Ballads Of Solar', 89.99, 3, None, 20.31, 11.42, -7.2, -6.32, sale_alert, expensive_alert)

# single(summary)

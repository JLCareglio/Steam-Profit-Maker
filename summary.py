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

    try:
        cheap_profit = cheap_card - game_price
        average_profit = average - game_price

        if cheap_profit > 0:
            cheap_profit = Fore.GREEN + "%.2f" % (cheap_profit)
            average_profit = Fore.GREEN + "%.2f" % (average_profit)

        elif average_profit > 0:
            cheap_profit = Fore.RED + "%.2f" % (cheap_profit)
            average_profit = Fore.GREEN + "%.2f" % (average_profit)

        else:
            cheap_profit = Fore.RED + "%.2f" % (cheap_profit)
            average_profit = Fore.RED + "%.2f" % (average_profit)

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
        + "\n🎴+Barato: {}$ARS	─  🎴+Caro: {}$ARS".format(
            price_cards.replace(",", " ||").split("||")[1].lstrip(" ARS$"),
            price_cards.replace(",", " ||").split("||")[-3].lstrip(" ARS$"),
        )
        + Fore.WHITE
    )
    print(
        Fore.CYAN
        + "Promedio: {} $ARS	─  Con el cromo barato: {} $ARS".format(
            average, cheap_card
        )
        + Fore.WHITE
    )

    if type(game_price) == float:
        print("\nProfit Cromo Barato	─	Profit Promedio")
        print("     {} $ARS		─          {} $ARS".format(cheap_profit, average_profit))

    print("\n📝 Precio de todos los cromos y su volumen de ventas:\n" + price_cards)

    return 0


def multi(app_ids, cheap_list, average_list, noprofit):

    os.system("clear")

    if len(cheap_list) + len(average_list) != 0:

        if len(cheap_list) > 0:
            print(
                f"""        {Fore.MAGENTA}= = = = = = = = = = = = = = = = = = = = = = =
        {Fore.WHITE}✅ Los siguientes {len(cheap_list)} juegos dan profit seguro:
        {Fore.MAGENTA}= = = = = = = = = = = = = = = = = = = = = = =\n"""
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
                f"""        {Fore.MAGENTA}= = = = = = = = = = = = = = = = = = = = = = =
        {Fore.WHITE}👀 Los siguientes {len(average_list)} juegos pueden dar profit:
        {Fore.MAGENTA}= = = = = = = = = = = = = = = = = = = = = = =\n"""
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
                f"""        {Fore.MAGENTA}= = = = = = = = = = = = = = = = = = = = = = =
        {Fore.RED}⛔ Los siguientes {len(noprofit)} juegos no dan profit:
        {Fore.MAGENTA}= = = = = = = = = = = = = = = = = = = = = = =\n"""
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

                print(f"{Fore.WHITE}🎮 {game_name}  ─  🔑 AppID: {app_id}\n")
                
            print(LINE_UP, end=LINE_CLEAR)

    else:
        print("⛔ Ningún juego de la lista da profit.")


# sale_alert = Fore.RED + '	ALERTA: Los cromos se venden muy poco (menos de 10 ventas en las ultimas 24 hs)' + Fore.WHITE
# expensive_alert = '\n        ' + Fore.RED + 'ALERTA: El juego posee uno o mas cromos muy caros que no se venden.' + Fore.WHITE

# summary = (302490, 'Ballads Of Solar', 89.99, 3, None, 20.31, 11.42, -7.2, -6.32, sale_alert, expensive_alert)

# single(summary)

import csv
import os
from datetime import datetime

from colorama import Back, Fore, Style, init
from dotenv import load_dotenv

import summary
from alerts import check
from price_ars import price_ars
from price_game import price_game
from sorter import sort
from summary import single

LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"


def single_scan(app_id):
    # load_dotenv()  # take environment variables from .env.
    # api_key = os.getenv("PROXIESAPI_AUTH_KEY")

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
        low_price_card = float(price_list[0][5:]) if price_list[0][5:] else 0.0
        high_price_card = float(price_list[-1][5:]) if price_list[-1][5:] else 0.0

        if expensive_cards > 0:
            for i in range(1, expensive_cards + 1):
                price_total -= float(price_list[-i][5:])

            expensive_alert = (
                "\n"
                + Fore.RED
                + "*Tiene uno o mas cromos muy caros que no se venden."
                + Fore.WHITE
            )

        average = round(
            cards_drop * (float(price_total) / float(cards_total)) * fees, 2
        )

        cheap_card = round(low_price_card * cards_drop * fees, 2)
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
            f"""{Fore.RED}
* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
💥 El ID {Fore.YELLOW}{app_id}{Fore.RED} no pudo escanearse por un error critico
{Fore.BLUE}💡 Para resolver el problema intente activar o cambiar de Proxy o VPN
📬 Si lo anterior no funciona, póngase en contacto con el desarrollador creando una issue en:
{Fore.GREEN}https://github.com/JLCareglio/Steam-Profit-Maker/issues
{Fore.RED}* * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""
        )
        app_data = {}
    print("")
    return app_data


def multi_scan(apps):
    #     load_dotenv()  # take environment variables from .env.
    #     api_key = os.getenv("PROXIESAPI_AUTH_KEY")
    #     if not api_key:
    #         api_key = input(
    #             f"""
    # {Fore.WHITE}Si tiene y quiere usar una api_Key de {Fore.GREEN}https://app.proxiesapi.com/{Fore.WHITE} colóquela a continuación, sino, solo pulse enter para continuar:
    # {Fore.YELLOW}"""
    #         )

    bad_app_id = []
    app_data = {}
    scanned_games = 1

    os.system("clear")
    print("⏳ Espere un momento...", end="\r")

    now = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
    cur_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(cur_path, "data")):
        os.makedirs(os.path.join(cur_path, "data"))
    file_path = os.path.join(cur_path, "data", f"Profit_Juegos_[{now}].csv")

    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "Nombre",
                "AppID",
                "Precio",
                "Cromo + Barato",
                "Cromo + Caro",
                "Cromos Obtenibles",
                "Profit Mínimo",
                "Profit Máximo",
                "Profit Promedio",
                "Comentarios",
                "Precio de todos los cromos y su volumen de ventas",
                "Fecha de Escaneo",
            ]
        )

        for app_id in apps:
            try:
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

            except Exception as e:
                success = False
                print(e)

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
                        + "*Tiene uno o mas cromos muy caros que no se venden."
                        + Fore.WHITE
                    )

                average = round(cards_drop * (price_total / cards_total) * fees, 2)

                low_price_card = float(price_list[0][5:]) if price_list[0][5:] else 0.0
                high_price_card = (
                    float(price_list[-1][5:]) if price_list[-1][5:] else 0.0
                )

                cheap_card = round(low_price_card * cards_drop * fees, 2)
                expensive_card = round(high_price_card * cards_drop * fees, 2)
                cheap_profit = "Profit con el cromo mas barato: No calculado"
                average_profit = "Profit promedio: No calculado"

                for i in range(len(price_list)):
                    price_cards += (
                        str(price_list[i]) + ", " + str(volume_list[i]) + " || "
                    )

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
                        + "Profit promedio: {} ARS$".format(
                            "%.2f" % (average - game_price)
                        )
                        + Fore.WHITE
                    )
                else:
                    average_profit = (
                        Fore.RED
                        + "Profit promedio: {} ARS$".format(
                            "%.2f" % (average - game_price)
                        )
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

                alerts = (
                    f"{sale_alert}{expensive_alert}".replace(Fore.GREEN, "")
                    .replace(Fore.YELLOW, "")
                    .replace(Fore.RED, "")
                    .replace(Fore.WHITE, "")
                )

                very_now = datetime.now().strftime("%d %b %Y %H:%M:%S")

                writer.writerow(
                    [
                        game_name,
                        app_id,
                        game_price,
                        low_price_card,
                        high_price_card,
                        cards_drop,
                        "%.2f" % (cheap_card - game_price),
                        "%.2f" % (expensive_card - game_price),
                        "%.2f" % (average - game_price),
                        alerts,
                        price_cards,
                        very_now,
                    ]
                )

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

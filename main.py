import os
import re

from colorama import Back, Fore, Style, init

from scan import multi_scan, single_scan
from sorter import sort_profit
from summary import multi, single


def main():

    rEspaciosSobrantes = re.compile(r"^\s+|\s+$|\s+(?=\s)")
    rSecuenciaNumérica = re.compile(r"\d+")

    init(autoreset=True)

    os.system("clear")

    apps = []
    lista_apps = {}

    while True:

        if len(apps) == 1:

            app_id = apps[0]

            if app_id in lista_apps:

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
                ) = lista_apps[app_id]
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
                print("")
            else:

                lista_apps.update(single_scan(app_id))
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
                ) = lista_apps[app_id]

        elif len(apps) > 1:
            app_ids = {}
            app_ids.update(multi_scan(apps))

            cheap_list, average_list, no_profit_list, error_list = sort_profit(app_ids)

            multi(app_ids, cheap_list, average_list, no_profit_list, error_list)

            lista_apps.update(app_ids)

        print(
            Style.BRIGHT
            + Fore.BLUE
            + "Puede introducir varios juegos separándoles por coma ',' o espacios"
        )
        apps = input(f"Introduzca los AppIDs o las URLs de los juegos:{Fore.YELLOW}\n")
        
        apps = re.sub(rEspaciosSobrantes, "", apps.replace(",", " ")).split(" ")
        apps = [
            rSecuenciaNumérica.search(x).group() if rSecuenciaNumérica.search(x) else x
            for x in apps
        ]

        datos_inválidos = [x for x in apps if not rSecuenciaNumérica.match(x)]
        apps = [x for x in apps if rSecuenciaNumérica.match(x)]

        if len(datos_inválidos) > 0:
            input(
                f"""
{Fore.RED}Los siguientes datos ingresados no son validos y serán ignorados:{Fore.WHITE}
{datos_inválidos}

{Fore.BLUE}Para mas información visite:
{Fore.GREEN}https://github.com/JLCareglio/Steam-Profit-Maker{Fore.WHITE}

Pulse enter para continuar..."""
            )

        # while apps == "*":
        #     print(
        #         "\nEl precio de los cromos y su volumen de ventas es de:\n\n"
        #         + price_cards
        #     )

        #     print(Style.BRIGHT + "\nPuede introducir varios ID separados por una ','")
        #     apps = input("Introduzca el App ID del juego: ")


main()

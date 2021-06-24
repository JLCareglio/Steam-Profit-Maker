from colorama import init, Fore, Back, Style
from scan import single_scan, multi_scan
from sorter import sort_profit
from summary import single, multi
import time, os


def main():

    init(autoreset=True)

    print(Style.BRIGHT + "\nPuede introducir varios ID separados por una coma ','")
    apps = input("Introduzca el App ID del juego: ")

    apps = apps.replace(' ','').split(',')


    lista_apps = {} 
    #lista_apps toma de identificador el ID del juego y separa los componentes de la siguiente forma
    #Nombre del Juego, Numero de cromos

    while True:


        if len(apps) == 1:

            app_id = apps[0]

            if app_id in lista_apps:

                game_name, game_price, cards_drop, price_cards, average, cheap_card, cheap_profit, average_profit, sale_alert, expensive_alert = lista_apps[app_id]
                summary = app_id, game_name, game_price, cards_drop, price_cards, average, cheap_card, sale_alert, expensive_alert
                single(summary)
                print("\nPara ver informacion de los cromos coloque '*'")

            else:

                lista_apps.update(single_scan(app_id))
                game_name, game_price, cards_drop, price_cards, average, cheap_card, cheap_profit, average_profit, sale_alert, expensive_alert = lista_apps[app_id]

                print("\nPara ver informacion de los cromos coloque '*'")

        elif len(apps) > 1:
            app_ids = {}
            app_ids.update(multi_scan(apps))

            cheap_list, average_list, noprofit = sort_profit(app_ids)

            multi(app_ids, cheap_list, average_list, noprofit)

            lista_apps.update(app_ids)



        print(Style.BRIGHT + "\n\nPuede introducir varios ID separados por una ','")
        apps = input("Introduzca el App ID del juego: ")

        while apps == '*':
            print('\nEl precio de los cromos y su volumen de ventas es de:\n\n' + price_cards)

            print(Style.BRIGHT + "\n\nPuede introducir varios ID separados por una ','")
            apps = input("Introduzca el App ID del juego: ")

        apps = apps.replace(' ','').split(',')




main()
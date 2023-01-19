from colorama import Back, Fore, Style, init


def check(price_list, volume_list):

    try:
        cheap_card_1 = float(price_list[0][5:])  # Card 1
    except:
        cheap_card_1 = float(price_list[0])

    try:
        cheap_card_2 = float(price_list[1][5:])  # Card 2
    except:
        cheap_card_2 = float(price_list[0])

    expensive_card_1 = float(price_list[-1][5:])  # Most Expensive Card
    expensive_card_2 = float(price_list[-2][5:])  # Second Expensive Card
    expensive_card_3 = float(price_list[-3][5:])  # Third Expensive Card

    try:
        expensive_card_4 = float(price_list[-4][5:])  # Four Expensive Card
    except:
        expensive_card_4 = float(price_list[-4])
    volume_1 = volume_list[-1]
    volume_2 = volume_list[-2]
    volume_3 = volume_list[-3]

    sales_flow = 0
    expensive = 0

    for volume in volume_list:
        sales_flow += volume

    # 	Alerta carta cara que no se vende.

    if expensive_card_3 > expensive_card_4 * 1.7 and volume_3 < 2:
        expensive = 3

    elif expensive_card_2 > expensive_card_3 * 1.7 and volume_2 < 2:
        expensive = 2

    elif (
        expensive_card_1 > expensive_card_2 * 1.5
        or expensive_card_1 > expensive_card_3 * 2
        and volume_1 < 2
    ):
        expensive = 1

    # 	Alerta si los cromos tienen flujo de ventas
    if sales_flow < 10:
        sales = (
            Fore.RED
            + "*Cromos se venden muy poco (menos de 10 ventas en las ultimas 24 hs)"
            + Fore.WHITE
        )

    elif sales_flow >= 10 and sales_flow <= 50:
        sales = Fore.YELLOW + "Cromos tienen algunas ventas" + Fore.WHITE

    elif sales_flow > 50 and sales_flow < 200:
        sales = Fore.GREEN + "Cromos se venden con frecuencia" + Fore.WHITE

    else:
        sales = Fore.GREEN + "Cromos se venden sin problemas" + Fore.WHITE

    return expensive, sales


"""price_list = ['ARS$ 3.56','ARS$ 4.56','ARS$ 5.56','ARS$ 6.56','ARS$ 7.56']
volume_list = [10,20,30,40,50]"""

"""tildes = 'á é í ó ú À È Ì Ò Ù'

print(tildes)
"""

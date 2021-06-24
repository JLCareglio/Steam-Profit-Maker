from colorama import *

init()

def single(summary):
	
	app_id, game_name, game_price, cards_drop, price_cards, average, cheap_card, sale_alert, expensive_alert = summary

	try:
		cheap_profit = round(cheap_card - game_price,2)
		average_profit = round(average - game_price,2)

		if cheap_profit > 0:
			cheap_profit = Fore.GREEN + str(cheap_profit)
			average_profit = Fore.GREEN + str(average_profit)

		elif average_profit > 0:
			cheap_profit = Fore.RED + str(cheap_profit)
			average_profit = Fore.GREEN + str(average_profit)

		else:
			cheap_profit = Fore.RED + str(cheap_profit)
			average_profit = Fore.RED + str(average_profit)

	except:
		cheap_profit = None
		average_profit = None


	print("\n 	" + Style.BRIGHT + Fore.BLUE + "App ID: {} ─ {} ─ Precio: {} ARS$".format(app_id, game_name, game_price) + Fore.WHITE)

	print("\n	Dropea {} cartas".format(cards_drop))
	print(Style.DIM +'{}{}'.format(sale_alert, expensive_alert) + Style.RESET_ALL)
	print(Fore.CYAN + "\n	Promedio: {}	ARS$	─    Con el cromo barato: {} ARS$".format(average, cheap_card) + Fore.WHITE)

	if type(game_price) == float:
		print("\n	Profit Cromo Barato	─	Profit Promedio")
		print(" 	     {} ARS$		─          {} ARS$".format(cheap_profit, average_profit))

	return 0

def multi(app_ids, cheap_list, average_list, noprofit):

	if len(cheap_list) + len(average_list) != 0:

		if len(cheap_list) > 0:
			print('Los siguientes {} juegos dan profit seguro:'.format(len(cheap_list)))

			print(Fore.MAGENTA + '	─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─') # 25

			for app_id in cheap_list:
				game_name, game_price, cards_drop, price_cards, average, cheap_card, cheap_profit, average_profit, sale_alert, expensive_alert = app_ids[app_id]

				summary = app_id, game_name, game_price, cards_drop, price_cards, average, cheap_card, sale_alert, expensive_alert

				single(summary)
				print(Fore.MAGENTA + '	─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─') # 25


		if len(average_list) > 0:
			print('Los siguientes {} juegos pueden dar profit:'.format(len(average_list)))

			for app_id in average_list:
				game_name, game_price, cards_drop, price_cards, average, cheap_card, cheap_profit, average_profit, sale_alert, expensive_alert = app_ids[app_id]

				summary = app_id, game_name, game_price, cards_drop, price_cards, average, cheap_card, sale_alert, expensive_alert

				single(summary)
				print(Fore.MAGENTA + '	─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─') # 25

		if len(noprofit) > 0:
			noprofit_ids = ''
			for noprofit_id in noprofit:

				noprofit_ids += noprofit_id + ' '

			print(Fore.RED + '\nLas siguientes ID no dan profit: {}'.format(noprofit_ids))

	else:
		print('Ningun juego de la lista da profit.')
		
	print('\nPara ver mas detalles introduzca la ID individualmente')





#sale_alert = Fore.RED + '	ALERTA: Los cromos se venden muy poco (menos de 10 ventas en las ultimas 24 hs)' + Fore.WHITE
#expensive_alert = '\n        ' + Fore.RED + 'ALERTA: El juego posee uno o mas cromos muy caros que no se venden.' + Fore.WHITE

#summary = (302490, 'Ballads Of Solar', 89.99, 3, None, 20.31, 11.42, -7.2, -6.32, sale_alert, expensive_alert)

#single(summary)
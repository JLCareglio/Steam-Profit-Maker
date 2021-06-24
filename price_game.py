from bs4 import BeautifulSoup
import requests
import json

def price_game(app_id, game_name):
	url = "https://store.steampowered.com/api/appdetails?appids=" + str(app_id) + "&cc=ars&filters=price_overview"
	datos = requests.get(url).content
	soup = BeautifulSoup(datos,features="html.parser")

	game_json = json.loads(str(soup))

	price_game = game_json[str(app_id)]["data"]["price_overview"]["final_formatted"]
	game_discount = game_json[str(app_id)]["data"]["price_overview"]["discount_percent"]

	price_game = price_game.replace('ARS$ ','').replace('.','').replace(',','.')

	"""if game_discount == 0:
		print("\nEl juego '{}' no se encuentra en descuento.\nEl valor del juego es {} ARS$".format(game_name, price_game))

	else:
		print("\nEl juego '{}' tiene un {}% de descuento.\nEl valor del juego en descuento es {} ARS$".format(game_name, game_discount, price_game))"""

	return float(price_game)

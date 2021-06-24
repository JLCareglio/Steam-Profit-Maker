from bs4 import BeautifulSoup
import requests, os

def get_market_hash (app_id, scanned_games, games_to_scan):

    url = "https://www.steamcardexchange.net/index.php?gamepage-appid-" + str(app_id)
    datos = requests.get(url).content
    soup = BeautifulSoup(datos,features="html.parser")

    market_hash = []

    trading_cards = int( soup.find('table', attrs={'class':'game-stats'}).th.text )
    card_images = soup.find_all('img', attrs={'class':'element-image'}, limit=trading_cards)
    game_name = soup.find('img', attrs={'class':'game-image'}) ['alt']

    os.system('cls')
    loaded_cards = 0
    loading_text = '\nCargando: {} cartas de {}'.format(loaded_cards, trading_cards)
    loading_bar = '─   [ ' + str('- ' * trading_cards).replace('-','■', loaded_cards) + ']   ─'

    print('App ID: ' + str(app_id) + '  ─  ' + 'Juego {} de {}'.format(scanned_games, games_to_scan))
    print(loading_text)
    print(loading_bar)

    for card_name in card_images:
    	if card_name.has_attr('alt'):

    		market_hash += str(app_id) + '-' + card_name['alt'],


    return market_hash, trading_cards, game_name
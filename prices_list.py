from bs4 import BeautifulSoup
from get_hash import get_market_hash
from colorama import init, Fore, Back, Style
import requests, json, time, os

def prices_list (app_id, games_to_scan, scanned_games):

    loaded_cards = 1

    try:
        market_hash, cards, game_name = get_market_hash(app_id, scanned_games, games_to_scan)

    except:
        market_hash = []
        cards = 0
        game_name = None

    prices = []
    volume_list = []
    success = True

    #market_hash = ['1140440-Pechenegs and Polovtsians', '1140440-OMON Soldier', '1140440-Riot Car', '1140440-Pay Respect to the President', '1140440-Bund of Karnavalny', '1140440-Agent "Cock"', '1140440-Erzhan', '1140440-Motorcade of the President', '1140440-Alien Invasion', '1140440-Soldier of FBK', '1140440-Ivan Temnoholmov', '1140440-Boris Haritonov', '1140440-Vladimir Vladimirovich', '1140440-"Are you a wolf?"', '1140440-Relaxing with friends', '1140440-Pechenegs and Polovtsians', '1140440-OMON Soldier', '1140440-Riot Car', '1140440-Pay Respect to the President', '1140440-Bund of Karnavalny', '1140440-Agent "Cock"', '1140440-Erzhan', '1140440-Motorcade of the President', '1140440-Alien Invasion', '1140440-Soldier of FBK', '1140440-Ivan Temnoholmov', '1140440-Boris Haritonov', '1140440-Vladimir Vladimirovich', '1140440-"Are you a wolf?"', '1140440-Relaxing with friends']
    #market_hash = ['302490-Dark Elf']

    for card_hash in market_hash:
        
        url = "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name=" + card_hash.replace(' ','%20')
        datos = requests.get(url).content
        soup = BeautifulSoup(datos,features="html.parser")
        card_json = json.loads(str(soup))

        points = '.' * (loaded_cards % 4)

        os.system('cls')
        loading_text = Fore.CYAN + 'Cargando: {} cartas de {}{}'.format(loaded_cards, cards, points)
        loading_bar = Fore.YELLOW + Style.DIM + '─   [ ' + Fore.WHITE + str('- ' * cards).replace('-',Fore.GREEN + '■' + Fore.WHITE, loaded_cards) + Fore.YELLOW + ']   ─' + Fore.WHITE

       
        print(Style.BRIGHT + 'App ID: ' + str(app_id) + '  ─  ' + 'Juego {} de {}\n'.format(scanned_games, games_to_scan))
        print(loading_text)
        print(loading_bar)

        loaded_cards += 1
        time.sleep(2.5)

        try:
            success = card_json['success']
        except:
            print('Problema con el cromo')
            pass

        if success == True:

            try:
                price_card = card_json['lowest_price']
            except:
                price_card = '0'
                print('Problema con el lowest_price')

            try:
                volume = card_json['volume']
            except:
                volume = '0'
                #print('Problema con el Volumen')

            prices += price_card.replace('.','').replace(',','.'),
            volume_list += volume,


        else:
            try:
                url += '%20%28Trading%20Card%29'
                datos = requests.get(url).content
                soup = BeautifulSoup(datos,features="html.parser")
                card_json = json.loads(str(soup))

                price_card = card_json['lowest_price']
                success = card_json['success']

                try:
                    volume = card_json['volume']
                except:
                    volume = '0'

                prices += price_card.replace(',','.'),
                volume_list += volume,


            except:
                volume = '0'
                price_card = '0'
                success = False

                break

    if len(market_hash) == 0:
            volume = '0'
            price_card = '0'
            prices = []
            volume_list = []
            cards = 0
            success = False

    

    return prices, volume_list, cards, success, game_name

#print(prices_list(280140, 0, 0))

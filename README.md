# Steam Profit Calculator
Introduces el appid de algun juego de steam y analizara las cartas del mismo en el mercado, dando datos detallados sobre si sale rentable o no, con promedios y alertas

Primero deben conseguir el App-Id de algun juego que tenga cromos, entran al buscador de steam y lo filtran por precio y juegos con cromos en el siguiente link: https://store.steampowered.com/search/?sort_by=Price_ASC&maxprice=70&category1=998&category2=29

![image](https://user-images.githubusercontent.com/86386696/123180991-cad87900-d462-11eb-816c-c04637d95754.png)

Ahi obtienen el ID del juego el cual introduciran en el programa de la siguiente forma:

![Parte 1](https://user-images.githubusercontent.com/86386696/123181030-daf05880-d462-11eb-9a0c-0d1bea839786.png)

El programa cargara datos de cada una de las cartas (tarda un ratito, por cuestiones que Steam permite una cierta cantidad de solicitudes por minuto, y si se exceden no te permite ingresar a la pagina de steam por unos minutos) el programa tiene el delay necesario para que esto no ocurra, una vez introducido el app ID cargara las cartas

![Parte 2 - Carga](https://user-images.githubusercontent.com/86386696/123181085-f65b6380-d462-11eb-9898-8b6aac1bf023.png)

Cuando termine de cargar las mismas mostrara un resumen completo con los datos extraidos

![Parte 3 - Resumen](https://user-images.githubusercontent.com/86386696/123181160-1c810380-d463-11eb-8b9a-feb9184fbab2.png)

En caso que el juego tenga cromos que no se venden, tambien lo advertira, y puedes revisar la lista de precios de los cromos colocando '*'

![image](https://user-images.githubusercontent.com/86386696/123182060-02482500-d465-11eb-84e4-a839a5d2db1d.png)




<p align="center">
  <img width="160" height="160" alt="CacheLib" src="https://em-content.zobj.net/thumbs/160/microsoft/319/coin_1fa99.png">
</p>
<h1 align="center"> SPM - Steam Profit Maker </h1>
<p align="left">
  <img src="https://img.shields.io/badge/license-GPL-blue">
  <img src="https://img.shields.io/badge/poetry-1.3-60A5FA?logo=poetry&color=60A5FA">
  <img src="https://img.shields.io/badge/python-v^3.9-3776AB?logo=python&color=3776AB">
  <img src="https://img.shields.io/badge/release%20date-pending-yellow">
  <img src="https://img.shields.io/badge/status-in%20development-yellow">
  <br>
  <img src="https://img.shields.io/github/stars/JLCareglio?style=social">
</p>

## Índice
* [Índice](#índice)
* [Descripción](#descripción)
* [Requisitos](#requisitos)
* [Primeros pasos](#primeros-pasos)
* [Ejemplo de uso](#ejemplo-de-uso)

## Descripción
<p>
  Herramienta para encontrar juegos rentables en Steam donde el precio de sus cromos supere el coste del propio producto 📈.
  <br>
  🤔 ¿Como funciona?, simple, solo introduces uno o varios AppIDs o URLs de juegos de steam y analizara los cromos del mismo en el mercado para luego dar datos detallados sobre si su compra es rentable, posibles ganancias y comentarios utiles 💪.
  <img src="https://user-images.githubusercontent.com/23004689/215903955-2bd0bf4f-83b9-4f22-a763-0a0687dd1643.png">
</p>

## Requisitos
- Python v3.9 o superior
- Tener instaladas las siguientes librerias:
  - beautifulsoup4
  - bs4
  - certifi
  - charset-normalizer
  - colorama
  - idna
  - python-dotenv
  - requests
  - soupsieve
  - urllib3
 - Terminal UNIX o PowerShell

Puedes usar el siguiente comando para instalar todas las librerias mensionadas:
```
pip3 install beautifulsoup4 bs4 certifi charset-normalizer colorama idna python-dotenv requests soupsieve urllib3
```

## Primeros pasos
1. Primero asegurate de cumplir con los [requisitos](#requisitos)
2. Clona el repositorio y abrelo desde una terminal compatible
```
git clone --depth 1 https://github.com/JLCareglio/Steam-Profit-Maker.git
cd ./Steam-Profit-Maker
```
3. Ejecuta main.py usando python 3.9 o superior
```
python3 main.py
```

## Ejemplo de uso

Busca ofertas de juegos que tengan cromos y guarda sus URLs o AppIDs, puedes encontrar una lista actualizada en la siguiente pagina:
[https://steamdb.info/sales/?min_reviews=0&min_rating=0&min_discount=0&category=29](https://steamdb.info/sales/?min_reviews=0&min_rating=0&min_discount=0&category=29)

Ingresa los juegos encontrados en el programa, ejemplo:
![Ingreso_Juegos](https://user-images.githubusercontent.com/23004689/211580693-bdda7b17-b752-425c-aad9-e5d30e9b81b7.png)

El programa cargara datos de cada una de las cartas (tarda un ratito, por cuestiones que Steam permite una cierta cantidad de solicitudes por minuto, y si se exceden no te permite ingresar a la pagina de steam por unos minutos) el programa tiene el delay necesario para que esto no ocurra, una vez introducido el app ID cargara las cartas
![Escaneo_Juegos](https://user-images.githubusercontent.com/23004689/211580984-308b6401-0b51-46df-a2fc-ecb0c62de7a6.png)

A medida que los juegos sean escaneados se van a ir mostrando y guardando sus datos
![Escaneo_Juegos_datos](https://user-images.githubusercontent.com/23004689/211581470-abb5af87-ba17-41d1-a2c8-82c253335251.png)
Para cada juego se mostraran algunos avisos y advertencias en caso de que tengan cromos que no se venden.

Cuando termine, veras un resumen completo con los datos extraidos, estaran ordenados en las siguientes 3 categorias:
![Resumen_Positivo](https://user-images.githubusercontent.com/23004689/211585266-40abdb15-d9fb-4e9c-81d8-848737aaeaa2.png)
![Resumen_Normal](https://user-images.githubusercontent.com/23004689/211585293-b799a919-6afb-4e5c-b857-36061b108646.png)
![Resumen_Negativo](https://user-images.githubusercontent.com/23004689/211585347-2a34a5d0-0300-4a33-8927-bbd1cebce043.png)

Tambien encontraras un informe dentro de la carpeta data en un archivo .csv con la fecha actual en la que comenzaste el escaneo de juegos. Puedes abrir y ver este archivo con algun programa como "Hojas de Calculo de Google".

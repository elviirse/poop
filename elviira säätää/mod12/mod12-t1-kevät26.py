#     Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
#     Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
#     Käyttäjälle on näytettävä pelkkä vitsin teksti.


import requests

vastaus = requests.get("https://api.chucknorris.io/jokes/random")
data = vastaus.json()

print(data["value"])


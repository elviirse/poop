# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan
# säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import json
import requests

oma_API = "3fd2be0aa3b3e83c3f04d2deeaeaf064"

while True:
    paikkakunta = input("Anna paikkakunta: ")

    pyyntö = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&units=metric&appid={oma_API}")
    # print(pyyntö.json())
    if pyyntö.json()['cod'] != 404:
        print('Virheellinen paikkakunta')
        continue
    else:
        lämpötila = round(pyyntö.json()['main']['temp'])

        print(f"Sää paikkakunnassa {paikkakunta} on tällä hetkellä {lämpötila}° astetta ")
    break
# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

noppa = int(input("Anna arpakuutioiden lukumäärä: "))

while noppa <=0:
    print("Pitää olla ainakin yksi noppa!")
    noppa = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(noppa):
    lukumaara = random.randint(1, 6)
    summa += noppa

print(f"Arpakuutioiden summa on: {summa}")
#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

random_luku = random.randint(1,10)
while True:
    user_input = int(input("Veikkaa luku väliltä 1-10: "))
    if user_input > random_luku:
        print("Liian suuri arvaus")
    elif user_input < random_luku:
        print("Liian pieni arvaus")
    elif user_input == random_luku:
        print("oikein")
        break

# mod03 t.1
# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen
# samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

fish_lenght = int(input("Kuinka pitkä kuhasi on (cm)? :"))

if fish_lenght >= 37:
    print("Saat pitää kuhasi.")
else:
    print(f"Kuhasi on {37-fish_lenght} cm alamittainen, palaute se takaisin järveen, kiitos.")
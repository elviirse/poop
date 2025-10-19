#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.


def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

def main():
    luvut = [3, 7, 8, 9, 11, 23, 67, 99]
    tulos = laske_summa(luvut)
    print(f"Listan {luvut} summa on {tulos}")

main()

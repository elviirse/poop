# Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

number1 = int(input("Syötä kokonaisluku: "))
number2 = int(input("Syötä toinen kokonaisluku: "))
number3 = int(input("Syötä kolmas kokonaisluku: "))

summa = number1 + number2 + number3
tulo = number1 * number2 * number3
keskiarvo = number1 + number2 + number3 / 3

print("Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo}")

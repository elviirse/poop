# mod 3 t.4
# kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi
# karkausvuosi.



year = int(input("Anna vuosiluku: "))

if year % 400 == 0 or ( year % 4 == 0 and year % 100 !=0) :
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausluku")


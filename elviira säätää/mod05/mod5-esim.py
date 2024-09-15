
name1 = "Ville"
name2 = "Liisa"
name3 = "Ulla"
age1 = 3
age2 = 5
age3 = 22
print(f"Hei {name1} ja ikäsi on {age1} vuotta")
print("---------")

names = ["Ville", "Liisa", "Ulla", "Anna", "Matti"]
ages = [age1, age2, age3, 45, 67]
print(names)
print(ages)






length = len(names)
print(f"Listan pituus on: {length}")

# names = ["Ville", "Liisa", "Ulla", "Anna", "Matti"]
# ages = [age1, age2, age3, 45, 67]


# alkioon viitataan indeksinumerolla
print(f"Hei {names[2]} ikäsi on {ages[2]}")

# viittaus listan ulkopuolelle tuottaa virheen
print("---------")


# listan läpikäynti while. silmukan avulla
iterator = 0

while iterator < len(names):
    print(f"Hei {names[iterator]} ikäsi on {ages[iterator]}")
    # iterator = iterator +1
    iterator +=1

# tapoja viitata listan alkioihin
lista = ["Ville", "Liisa", "Ulla", "Anna", "Matti", "Ahmed", "Neo", "Viivi"]
print(lista[2:5]) # 2, 3, 4 (ei viimeistä alkiota mukaan), 3 alkiota indeksistä alkaen
print(lista[2:]) # kaikki loput alkiot indeksillä 2 alkaen
print(lista[-1]) # liatan viimeinen alkio
print(lista[2:6:2]) #indeksistä 2 indeksiin 6, joka toinen
print(lista[-1:-3:-1])


# listaan vi yhdistää ja siellä voi olla erilaisia tietorakenteita
lista1 = ["Ulla", "Matti", "Ilkka"]
yhdistetty_lista = [23, 45, 66, 67, 67, lista1]
print(yhdistetty_lista)
print(yhdistetty_lista[5][0])

print("\n-----------")
print("LISTAOPERAATIOT")


# lista = ["Ville", "Liisa", "Ulla", "Anna", "Matti", "Ahmed", "Neo", "Viivi"]

lista.append("Uusi nimi")
print(lista)


if "Ulla" in lista:
    print("Ulla löytyi listasta! Ja nyt se poistetaan sieltä.")
    lista.remove("Ulla")
    print(lista)

# pistetään nimi ulla takaisin ensimmäiseksi listan alkioksi
lista.insert(0, "Ulla")
print(lista)

# monentenako lisätty nimi nyt on
print(lista.index("Matti"))

lisaa_nimia = ["Ines", "Aku", "Tupu", "Lupu"]
lista.extend(lisaa_nimia)
# uusi_lista = lista + lisaa_nimia
print(lista)

lista[2] = "Tyhmä-Liisa" # muokataan olemassa olevaa alkiota
print(lista)
lista.sort()
print(lista)

print("\n-----------")
print("Listan läpikäynti for-toistorakenteen avulla\n")


for kirjain in "abcde":
    print(kirjain)

for alkio in [1, 2, 3, 4, 5]:
    print(alkio)

for nimi in lista:
    print(nimi)
"""
for numero in range(5, 50, 5):
    print(numero)

print("------")
for i in range(999, 0, -30):
    print(i)
"""
# käytetään edellä olevia iteroimaan nimilistaa läpi
# for silmukka iteraattorilla

print(lista)
for i in range(5):  # 0,1,2,3,4
    print(i)
    print(f"Terve: {lista[i]}")

print("------")
print("Listan pituus rangena:")

listan_pituus = len(lista)
print(f"Lista on {listan_pituus} alkiota pitkä")

for i in range(listan_pituus): # listan pituus maksimina 0-12
# for i in rnage(len(lista)):
     print(f"Terve: {lista[i]}")


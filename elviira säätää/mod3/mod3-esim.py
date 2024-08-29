# Alustus ehtolauseille
"""
rahat = float(input("Anna rahamääräsi: "))

if rahat >= 5:
   # print("Voit ostaa latten")


print("Jatketaan pääohjelmaa")

# sama kuin

rahat = float(input("Anna rahamääräsi: "))

##print(ehto)




luku = int(input("Anna luku: "))
if luku >=0:
    print("Luku on positiivinen")

if luku <0:
    print("Luku on negatiivinen")

# kaksi toisensa poissulkevaa vaihtoehtoa
rahat = float(input("Anna rahamääräsi: "))
if rahat >= 5:
    print("Voit ostaa latten")
else:
    print("Sinulla ei ole tarpeeksi rahaa")

# monta vaihtoehtoa

user_input = input("Valitse a, b, tai c: ")
if user_input == "a":
    print("Tehdään jotain, käyttäjä valitsi kirjaimen a")
elif user_input == "b":
    print("Tehdään jotain muuta kivaa, käyttäjä valitsi b")
elif user_input == "c":
    # lohkossa on usein paljonki koodia, kaikki sisännetty suoritetaan
    print("käyttäjä valitsi c")
    print("Voitit jackpotin")
    a = 169 +4
    print(f"voitit rahaa {a} euroa")
else:
    print("Käyttäjä ei syöttänyt a, b tai c. Invalid answer.")

print("Ohjelma loppuu, heihei")
"""
# loogiset operaattorit

ika = 5
nimi = "Elviira"
# True True
print(ika < 10 and nimi == "Elviira")
# True False
print(ika < 10 and nimi == "Einari")

print(ika < 10 or "Einari")

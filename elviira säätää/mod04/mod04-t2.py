# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm


annettu_luku = float(input("Anna tuumasi: "))
luku = annettu_luku * 2.54

while luku >0:
    print(f"Tuumasi senttimetreinä on: {luku}")
    break
else:
    print("Ohjelma lopetetaan")




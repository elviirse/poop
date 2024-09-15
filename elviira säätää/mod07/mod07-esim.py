#oppilaat ["Ulla"] = 22
#print(oppilaat)

nimet = ["Viivi", "Ahmed"]
numerot = ["050-1234567", "040-1112223"]

#print(f"{nimet[0]}, numero: {numerot[0]}")

yhteystiedot = {"Viivi": "050-1234567", "Ahmed": "040-1112223"}
#print(f"{yhteystiedot['Viivi']}")
hakusana = input("Puhelinnumerohaku, anna nimi: ")
# listojen avulla, selvitetään ensin oikea indeksi
index = nimet.index(hakusana)
print(f"{hakusana}, numero: {numerot[index]}")
# sanakirjalla, hyödynnetään avainta
print(f"{hakusana}, numero: {yhteystiedot[hakusana]}")



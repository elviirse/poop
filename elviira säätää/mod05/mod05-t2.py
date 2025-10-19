# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla
# sort-metodille argumentiksi reverse=True.

luvut = []

user_input = input("Syötä luku tai lopeta tyhjällä merkkiluvulla: ")

while user_input != "":
    luvut.append(float(user_input))
    user_input = input("Syötä luku tai lopeta tyhjällä merkkiluvulla: ")

luvut.sort(reverse=True)

print("suurimmat luvut:")
for luku in luvut[:5]:
    print(luku)
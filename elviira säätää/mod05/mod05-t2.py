# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla
# sort-metodille argumentiksi reverse=True.

luvut = []


while True:
    user_input = input("Syötä luku tai lopeta tyhjällä merkkijonolla: ")

if user_input == "":
   break

   

luvut.sort(reverse=True)


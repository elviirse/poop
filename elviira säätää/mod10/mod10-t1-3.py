# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan
# alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan
# määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä,
# joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi
# ja talon hisseillä ajelemiseksi.

#t.1
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        #nykyinen kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.kerros:
            # olion omia metodeita kutsuttuaessa käytetään self.
            while kohdekerros > self.kerros:
                self.kerros_ylos()
        elif kohdekerros < self.kerros:
            while kohdekerros < self.kerros:
                self.kerros_alas()
    def kerros_ylos(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1
        return

#t.2
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumaara = hissien_lukumaara
        self.hissit = []
        for i in range(3):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissin_numero = hissin_numero
        if 0 <= hissin_numero < self.hissien_lukumaara:
            print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohdekerros}.")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)


# t.3
    def palohalytys(self):
        print("Palohälytys")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


# t.1
h = Hissi(2,10)
h.siirry_kerrokseen(4)
print(f"Hissi on kerroksessa {h.kerros}")
h.siirry_kerrokseen(1) # ei toimi vielä
print(f"Hissi on kerroksessa {h.kerros}")

#t.2
t = Talo (2, 10, 3 )
t.aja_hissia(1,9)
t.aja_hissia(4,5)
t.aja_hissia(2,10)

#t.2
t.palohalytys()
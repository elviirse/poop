#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä,
# joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.kerros:
            while kohdekerros > self.kerros:
                self.kerros_ylos()
        elif kohdekerros < self.kerros:
            while kohdekerros < self.kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        self.kerros +=1

    def kerros_alas(self):
        self.alin_kerros -=1
        return

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumaara = hissien_lukumaara
        self.hissit = []
        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissin_numero = hissin_numero
        if 0 <= hissin_numero < self.hissien_lukumaara:
            print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohdekerros}.")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)


# pääohjelma

h = Hissi(alin_kerros=2, ylin_kerros=12)
h.siirry_kerrokseen(kohdekerros=5)
print(f"Hissi on kerroksessa {h.kerros}")
h.siirry_kerrokseen(kohdekerros=7)
print(f"Hissi on kerroksessa {h.kerros}")

t = Talo(alin_kerros=2, ylin_kerros=12, hissien_lukumaara=4)
t.aja_hissia(hissin_numero=3, kohdekerros=7)
t.aja_hissia(hissin_numero=1, kohdekerros=12)

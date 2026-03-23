# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.





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

    def palohalytys(self):
        print("Palohälytys")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)



# pääohjelma

h = Hissi(alin_kerros=2, ylin_kerros=12)
h.siirry_kerrokseen(kohdekerros=5)
print(f"Hissi on kerroksessa {h.kerros}")
h.siirry_kerrokseen(kohdekerros=7)
print(f"Hissi on kerroksessa {h.kerros}")

t = Talo(alin_kerros=2, ylin_kerros=12, hissien_lukumaara=4)
t.aja_hissia(hissin_numero=3, kohdekerros=7)
t.aja_hissia(hissin_numero=1, kohdekerros=12)

t.palohalytys()


"""
Tässä on esimerkki olio-ohjelmoinnin periytymisestä.

Polkupyörä-luokalla on ominaisuudet polkupyörän merkki ja vaihteiden lukumäärä.
Tee luokalle konstruktori, jossa voit asettaa nämä arvot.
Tee luokalle myös metodi tulosta(), joka tulostaa polkupyörän kaikki tiedot.

Tee myös luokka Sähköpyörä, joka periytyy Polkypyörä-luokasta.
Sähköpolkupyörä-luokalla on lisäksi ominaisuudet omistaja sekä toimintasäde sähköllä.
Hyödynnä aliluokassa (Sähköpolupyörä) sen yliluokan (Polupyörä) valmiita koodeja.

Tee pääohjelma, jossa luot polkypyörän ja tulostat sen kaikki ominaisuudet.
Tee lisäksi sähköpolupyörä ja tulosta sen kaikki ominaisuudet.
"""

class Polkupyörä:
    def __init__(self, merkki, vaihteiden_lukumaara):
        self.merkki = merkki
        self.vaihteiden_lukumaara = vaihteiden_lukumaara

    def tulosta(self):
        print("Polkypyörän tiedot: ")
        print(f"Polkupyörän merkki: {self.merkki}")
        print(f"Vaihteiden lukumäärä: {self.vaihteiden_lukumaara}")
        return

class Sähköpyörä(Polkupyörä):
    def __init__(self, merkki, vaihteiden_lukumaara, omistaja, toimintasade):
        # kutsutaan yliluokan (pyörän) alustajaa
        super().__init__(merkki, vaihteiden_lukumaara)
        self.omistaja = omistaja
        self.toimintasade = toimintasade

    def tulosta(self):
        # 'ylikirjoitetaan' yliluokan metodi
        # hyödynnetään aluksi yliluokan valmista toimintoa
        super().tulosta()
        # tulostetaan lisäksi puuttuvat tiedot
        print(f"Omistaja: {self.omistaja} ")
        print(f"Toimintasäde: {self.toimintasade} ")



eka_pyörä = Polkupyörä(merkki="Helkama", vaihteiden_lukumaara= 3)
eka_pyörä.tulosta()

toka_pyörä = Sähköpyörä(merkki="Tunturi", vaihteiden_lukumaara= 21,omistaja= "Mie", toimintasade= 40)
toka_pyörä.tulosta()



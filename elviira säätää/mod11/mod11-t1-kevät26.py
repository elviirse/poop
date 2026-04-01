# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
# joka tulostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.


class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print("Kirjan tiedot:")
        print(f"Kirjan nimi: {self.nimi}")
        print(f"Kirjoittajan nimi: {self.kirjoittaja}")
        print(f"Kirjan sivumäärä: {self.sivumaara}")
        return



class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimmittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimmittaja

    def tulosta_tiedot(self):
        print("Lehden tiedot:")
        print(f"Lehden nimi: {self.nimi}")
        print(f"Lehden päätoimittaja: {self.paatoimittaja}")
        return

# Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).

julkaisu1 = Kirja("Hytti n:o 6", "Rosa Liksom", "200")
julkaisu1.tulosta_tiedot()

julkaisu2 = Lehti("Aku Ankka", "Aki Hyyppä")
julkaisu2.tulosta_tiedot()


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
    # lisää arvo self nopeuteen
        self.nopeus += muutos
    # tarkasta ettei nopeus oli yli
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # tarkasta ettei nopeus ole alle 0
        elif self.nopeus < 0:
            self.nopeus = 0


    def kulje(self, aika):
    # laske kuinka paljon auto on kulkenut annetussa ajassa tietyllä ajalla
        self.matka += self.nopeus * aika
    # lisää kuljettu matka kokonaismatkaan


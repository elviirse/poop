# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.


vuodenajat = ("talvi", "talvi", "talvi",
              "kevät", "kevät", "kevät",
              "syksy", "syksy", "syksy")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    indeksit = (kuukausi % 12)
    vuodenaika = vuodenajat[indeksit]
    print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika}")


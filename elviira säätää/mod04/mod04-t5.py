# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

username = "python"
password = "rules"

round_counter = 0
max_rounds = 5

while round_counter < max_rounds:
    user_username = input("Käyttäjätunnus: ")
    user_password = input("Salasana: ")

    if username == user_username and password == user_password:
        print(f"Tervetuloa.")
        break

    else:
        round_counter += 1
        print(f"Käyttäjätunnus ja/tai salasana on väärin. Yritä uudestaan.")

if round_counter == max_rounds:
    print("Pääsy evätty")

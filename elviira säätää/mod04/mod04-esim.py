# while-silmukat (loopit)
# ikuinen silmukka, ei hyvä!
"""
while True:
    print("Moro")
    print("Elviira")

max_count = int(input("Montako kertaa pöötään?"))
counter = 0
while counter < max_count:
    counter = counter + 1
    print(f"{counter}. Kerran Pöö!")
print(f"Laskurin arvo lopuksi: {counter}")
"""
import random

# noppasimulaattori (import random)
# mikä on kahden yhtäaikaisen kutosen todennäköisyys
rounds = 1000
round_counter = 0
total_rolls = 0
while round_counter < rounds:
    round_counter += 1
    die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter +=1
        die1 = random.randint(1,6)
        die2 = random.randint(1, 6)
        # print(f"{roll_counter}. heiton silmäluvut: {die1} ja {die2}")
    # print(f"Noppia heitettiin {roll_counter} kertaa")
    total_rolls = total_rolls + roll_counter
print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla.")


# ohjelma komentorivikakäyttöliittymällä
# (valikkosovellus, johon sisälletty ylläoleva härdelli)
command = ""
while command != "lopeta":
    command = input("Komento, kiitos>")
    if command == "lopeta":
        print("Lopetetaan.")
        # break # "heittää ulos" silmukasta, ei paras
    elif command == "Pöö":
        max_count = int(input("Montako kertaa pöötään?"))
        counter = 0
        while counter < max_count:
            counter = counter + 1
            print(f"{counter}. Kerran Pöö!")
        print(f"Laskurin arvo lopuksi: {counter}")
    elif command == "noppa":
        rounds = 1000
        round_counter = 0
        total_rolls = 0
        while round_counter < rounds:
            round_counter += 1
            die1 = die2 = roll_counter = 0
            while die1 < 6 or die2 < 6:
                roll_counter += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
            total_rolls = total_rolls + roll_counter
        print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla.")


    else:
        print("En ymmärrä komentoa. Yritä uudestaan, kiitos.")
print("Ohjelma sammutettu.")
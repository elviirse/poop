

# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
    # Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    # Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

user_input = input("Syötä sukupuolesi: ")

if user_input == "nainen":
    user_input = int(input("Syötä hemoglobiiniarvosi (g/l): "))
    if user_input > 175:
        print("Hemoglobiiniarvosi on korkea.")
    elif user_input < 117:
        print("Hemoglobiiniarvosi on alhainen")
    elif  117 <= user_input < 175:
        print("Hemoglobiiniarvosi on normaali")

if user_input == "mies":
    user_input = int(input("Syötä hemoglobiiniarvosi (g/l): "))
    if user_input > 195:
        print("Hemoglobiiniarvosi on korkea.")
    elif user_input < 134:
        print("Hemoglobiiniarvosi on alhainen")
    elif 134 <= user_input < 195:
        print("Hemoglobiiniarvosi on normaali")

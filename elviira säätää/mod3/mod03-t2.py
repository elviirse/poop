# mod03 t.2
# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

    #LUX on parvekkeellinen hytti yläkannella.
    #A on ikkunallinen hytti autokannen yläpuolella.
    #B on ikkunaton hytti autokannen yläpuolella.
    #C on ikkunaton hytti autokannen alapuolella.

#jos käyttäjä syöttää kelvottoman hyttiluokan,
# ohjelma tulostaa Virheellinen hyttiluokka.

user_input = input("Valitse hyttiluokka LUX, A, B tai C: ")
if user_input == "LUX":
    print("Valitsit hyttiluokan: LUX")
    print("LUX on parvekkeellinen hytti yläkannella.")
elif user_input == "A":
    print("Valitsit hyttiluokan: A")
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif user_input == "B":
    print("Valitsit hyttiluokan: B")
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif user_input == "C":
    print("Valitsit hyttiluokan: C")
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")
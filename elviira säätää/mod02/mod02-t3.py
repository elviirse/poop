# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

number1 = int(input("Syötä suorakulmion kanta: "))
number2 = int(input("Syötä suorakulmion korkeus: "))

piiri = 2 * number1 + 2 * number2
pintaala = number1 * number2

print(f"Suorakulmion piiri on: {piiri}")
print(f"Suorakulmion pinta-ala on: {pintaala}")
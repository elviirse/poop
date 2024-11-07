"""
# mod05 t.1 varten

nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(nimet)
---
# youtube vidi
birth_year = input("minä vuonna synnyit?: ")
age = 2024 - int(birth_year)
print(age)


num1 = input("first: ")
num2 = input("second: ")
sum = float(num1) + float(num2)
print("sum: " + str(sum))

user_input = int(input("Paino: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = user_input / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = user_input * 0.45
    print("weight in kgs:" + str(converted))

"""

name = input("Mikä on sinun lempi ruoka?: ")
print(name + " . Elviira ei haise:) toisten päin ja lukko ")
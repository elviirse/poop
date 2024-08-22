# syötteen lukeminen ja sijoittaminen muuttujaan
name = input("Anna nimesi: ")
# name = "Elviira" # merkkijono (string)
print("Moi \n " + name) # "Moi " + "Elviira" -> "Moi Elviira"

# age = "22"
age = input("Anna ikäsi: ")
print("Ikäsi on " + age)
age = int(age) + 1
age_string = str(age) # muutetaan int -> string, esim. 8 -> "8"
print("Ikäsi on vuoden päästä " + age_string)
age = age + 1
print("Ikäsi on kahden vuoden päästä " + str(age))


# käyttäjän pituus metreinä, liukuluku (float)
# height = 1.7
height = float(input("Anna pituus: "))

height = height + 0.1
print(f"Nimi: {name}, Ikä: {age}, Pituus: {height} ")

import math
print("pi: ")
print(math.pi)
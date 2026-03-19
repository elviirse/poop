from classes.auto import Auto

auto1 = Auto("ABC-123",142)

auto1.kiihdyta(30)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto1.nopeus} km/h")

auto1.kiihdyta(70)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto1.nopeus} km/h")

auto1.kiihdyta(50)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto1.nopeus} km/h")

auto1.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto1.nopeus} km/h")
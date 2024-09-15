# funktio-esimerkkejä
"""

def do_something():
    print("Doing")
    print("something")
    return "tässä on palautettava arvo, voi olla ihan minkä tyyppinen vaan"

return_value = do_something()
print(return_value)

# funktio, jolla parametrejä (argumentti)
def combine_strings(string1, string2):
    combination = f"{string1}, {string2}"
    #print(combination)
    return combination

print(combine_strings("auto", "ajaa"))

combination = combine_strings("kuski", "jarruttaa")
combination = combine_strings(combination, "nopeasti")
print(combination)


# yksinkertainen laskin, joille voi antaa vain tasan 2 parametriä
def calculate_sum(calc_type, number1, number2):
    if type == "sum":
        return number1 + number2
    elif type == "division":
        return number1 / number2
    # return None # oletustoiminnallisuus

print(calculate("sum",2.4, 3.5))
print(calculate("division", 2.4, 8))
from functools import total_ordering


# listat ja funktiot
def calculate_sum(numbers):
    total_sum = 0
    #for i in range(len(numbers)):
    #    total_sum = total_sum + numbers[i]
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

nums = [3, 4, 5]
print(calculate_sum(nums))

print(calculate_sum([3, 4, 5, 10]))

calculate_sum([3, 4, 5])

"""

# vaihtuva määrä parametrejä
# * tekee kaikista syötetyistä parametreistä (arvoista) listan
# ja sijoittaa listan numbers-muuttujaan
def calculate_sum2(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

print(calculate_sum2(2, 3, 8, -10, 4.67, 11.33))

# extra: nimetyt parametrit ja oletusarvot
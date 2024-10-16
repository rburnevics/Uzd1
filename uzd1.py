import math

x = float(input("Ievadiet skaitli x: "))
y = float(input("Ievadiet skaitli y: "))

if y != 0 and x != 0:
    izteiksme_1 = (2 + x) / (x * y)
    print(f"(2 + {x}) / ({x} * {y}) = {izteiksme_1}")
else:
    print("Nav iespējams dalīt ar nulli izteiksmē 1")

izteiksme_2 = 5 * x**3 - x**2 + 7 * x - 6
print(f"5 * {x}^3 - {x}^2 + 7 * {x} - 6 = {izteiksme_2}")

if x * y >= 0:
    izteiksme_3 = math.sqrt(x * y)
    print(f"√({x} * {y}) = {izteiksme_3}")
else:
    print("Nav iespējams aprēķināt kvadrātsakni no negatīva skaitļa izteiksmē 3")

if y != 0:  
    izteiksme_4 = (2 ** (x * y)) / (5 * y)
    print(f"(2^({x} * {y})) / (5 * {y}) = {izteiksme_4}")
else:
    print("Nav iespējams dalīt ar nulli izteiksmē 4")

import math

def ievadit_skaitli(teksts):
    while True:
        try:
        
            skaitlis = float(input(teksts))
            return skaitlis
        except ValueError:
            print("Lūdzu, ievadiet derīgu skaitli!")

x = ievadit_skaitli("Ievadiet skaitli x: ")
y = ievadit_skaitli("Ievadiet skaitli y: ")


if y != 0 and x != 0:
    izteiksme_1 = (2 + x) / (x * y)
    print(f"(2 + {x}) / ({x} * {y}) = {izteiksme_1}")
else:
    print("Nav iespējams dalīt ar nulli izteiksmē 1")


izteiksme_2 = 5 * x**3 - x**2 + 7 * x - 6
print(f"5 * {x}^3 - {x}^2 + 7 * {x} - 6 = {izteiksme_2}")


if x * y >= 0:  
    izteiksme_3 = math.sqrt(x * y)
    print(f"√({x} * {y}) = {izteiksme_3}")
else:
    print("Nav iespējams aprēķināt kvadrātsakni no negatīva skaitļa izteiksmē 3")


if y != 0:
    izteiksme_4 = (2 ** (x * y)) / (5 * y)
    print(f"(2^({x} * {y})) / (5 * {y}) = {izteiksme_4}")
else:
    print("Nav iespējams dalīt ar nulli izteiksmē 4")

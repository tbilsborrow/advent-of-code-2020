total = 0

def calcfuel(mass):
    fuel = int(mass / 3) - 2
    if fuel < 0:
        fuel = 0
    elif fuel > 0:
        fuel += calcfuel(fuel)
    return fuel

with open("input1.txt", "r") as f:
    for l in f:
        mass = int(l.strip())
        total += calcfuel(mass)

print(total)

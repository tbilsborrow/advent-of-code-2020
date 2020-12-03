total = 0

with open("input1.txt", "r") as f:
    for l in f:
        mass = int(l.strip())
        fuel = int(mass / 3) - 2
        total += fuel

print(total)

import sys

input = [line.strip() for line in sys.stdin]

validCount = 0
for s in input:
    # ugly AF should've just done regex oh well
    a = s.split();

    [min, max] = [int(n) for n in a[0].split('-')]

    ch = a[1][0]

    password = a[2]

    count = len(list(filter(lambda z : z == ch, password)))

    if count >= min and count <= max:
        validCount += 1

print(validCount)

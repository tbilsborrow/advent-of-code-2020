import sys

input = [line.strip() for line in sys.stdin]

validCount = 0
for s in input:
    # ugly AF should've just done regex oh well
    a = s.split();

    [min, max] = [int(n) for n in a[0].split('-')]

    ch = a[1][0]

    password = a[2]

    if (password[min-1] == ch and password[max-1] != ch) \
            or (password[min-1] != ch and password[max-1] == ch):
        validCount += 1

print(validCount)

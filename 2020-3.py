import sys

input = [line.strip() for line in sys.stdin]

def sled(dx, dy):
    numtrees = 0
    # yes errors on blank input line
    r = c = 0
    while r < len(input):
        if c >= len(input[r]):
            # wrap around
            c = c - len(input[r])
        if input[r][c] == '#':
            numtrees += 1
        r += dy
        c += dx
    return numtrees

# part 1
print(sled(3, 1))

# part 2
print(sled(1, 1) * sled(3, 1) * sled(5, 1) * sled(7, 1) * sled(1, 2))

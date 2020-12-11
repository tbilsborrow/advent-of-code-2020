import sys

input = [int(line.strip()) for line in sys.stdin]

PREAMBLE_LENGTH = 25

def isvalid(num, l):
    seen = set()
    for entry in l:
        if num - entry in seen: return True
        seen.add(entry)
    return False

# part 1 - 20874512
for i in range(PREAMBLE_LENGTH, len(input)):
    buffer = input[i - PREAMBLE_LENGTH:i]
    if not isvalid(input[i], buffer):
        invalid = input[i]
        break

print(f'part 1: {invalid}')

# part 2 - 3012420

# this assumes valid input (ie. an answer exists)
# if not, infinite loops and list indexing errors abound
i = 0
j = 1
sum = input[i] + input[j]
while True:
    while sum < invalid:
        j += 1
        sum += input[j]
    while sum > invalid:
        sum -= input[j]
        j -= 1
    if sum == invalid:
        rmin = min(input[i:j+1])
        rmax = max(input[i:j+1])
        print(f'part 2: {rmin + rmax} (from {i} to {j})')
        break
    sum -= input[i]
    i += 1

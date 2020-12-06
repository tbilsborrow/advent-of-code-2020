import sys

input = [line.strip() for line in sys.stdin]

def traverse(s, chlo, chhi, lo, hi):
    if lo == hi: return lo
    if s[0] == chlo: return traverse(s[1:], chlo, chhi, lo, int((lo+hi)/2))
    return traverse(s[1:], chlo, chhi, int((lo+hi+1)/2), hi)

ids = set(traverse(s[0:7], 'F', 'B', 0, 127) * 8 + traverse(s[7:10], 'L', 'R', 0, 7) for s in input)

# part 1
m = max(ids)
print(m)

# part 2 (assume just one is missing)
while m in ids: m -= 1
print(m)

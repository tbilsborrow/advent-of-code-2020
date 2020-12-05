import sys
import re

def validateheight(h):
    if not h[:-2].isnumeric(): return False
    if h.endswith('cm'): return 150 <= int(h[:-2]) <= 193
    if h.endswith('in'): return 59 <= int(h[:-2]) <= 76
    return False


colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

required = {
    'byr': lambda v: v.isnumeric() and 1920 <= int(v) <= 2002,
    'iyr': lambda v: v.isnumeric() and 2010 <= int(v) <= 2020,
    'eyr': lambda v: v.isnumeric() and 2020 <= int(v) <= 2030,
    'hgt': validateheight,
    'hcl': lambda v: re.search('^#[0-9a-f]{6}$', v),
    'ecl': lambda v: v in colors,
    'pid': lambda v: len(v) == 9 and v.isnumeric(),
}


def validate(passport):
    # print(passport)
    if not set(required).issubset(passport): return False

    # all fields are present, check the values
    for k,v in passport.items():
        if k in required and not required[k](v):
            return False

    # all fields successfully validated
    return True
    

numvalid = 0
passport = {}
for line in sys.stdin:
    if not line.strip():
        # previous passport fully read in - now validate
        if validate(passport): numvalid += 1
        passport = {}
    else:
        passport.update([v.split(':') for v in line.split()])

# don't forget the last one
if validate(passport): numvalid += 1

print(numvalid)

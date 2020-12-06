import sys
from functools import reduce

def toset(str):
    return {ch for ch in str}

def reducestrings(strings):
    '''reduce to set of chars appearing in all strings'''
    return reduce(lambda a, b: a & toset(b), strings, toset(strings[0]))

# each group is a list of strings
groups = [g.strip().split('\n') for g in sys.stdin.read().split('\n\n')]

sets = [reducestrings(g) for g in groups]

print(sum(len(s) for s in sets))

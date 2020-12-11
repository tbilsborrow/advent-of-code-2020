import sys
import collections
import math
import itertools

def slider(list, num):
    d = collections.deque([], num)
    for item in list:
        d.append(item)
        if len(d) == num:
            yield d

input = sorted([int(line.strip()) for line in sys.stdin])
# add starting 0 and ending (max+3)
input = [0] + input + [input[len(input)-1]+3]

# list of sliding pairwise diffs
diffs = [x[1]-x[0] for x in slider(input, 2)]

# part 1: 2470
print(diffs.count(1) * (diffs.count(3)))

# part 2: 1973822685184

def magic(n):
    return max(1,math.pow(2,n-2) - (n-3) * ((n-4)/2))

# list of size+1 of runs of consecutive 1s
# ignoring 3s because for two numbers 3 apart there's only one way to get from a->b
# assuming no 2s in here
# looking at runs of 1s because I want to determine the number of paths through each run
#   the +1 is to catch the last 1 in the run
#   example input: [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
#           diffs: [1, 3, 1, 1, 1, 3, 1,  1,  3,  1,  3]
#         oneruns: [2,    4,          3,          2]
oneruns = [len(list(g))+1 for k, g in itertools.groupby(diffs) if k == 1]

# magic formula to get number of valid permutations for each run of 1s
magics = [magic(n) for n in oneruns]

# multiply them all together for total number of permutations
print(int(math.prod(magics)))


# -------------------------------------------------------------------
# examining lists of consecutive numbers
# first and last number stay put, middle numbers may be removed

# 2 numbers means you cannot remove any, there is but one path from a->b

# 3 numbers means you can remove 1 (n-2) which yields one additional path + the original
# n=3 means 2 total
# 4 5 6
# 4 6

# with 2 numbers to remove you get 2 subsets of 3 numbers, which each yield 1 more path, but 1 is duplicate (x)
# n=4 means 4 total
#  4 5 6 7
#  4 5 7
#  4 7
#  4 6 7
# x4 7

# with 3 numbers to remove, you get 3 subsets of 4 numbers
# - subset #1 gives 4 unique paths (2^(n-3))
# - subset #2 gives 2 more unique paths (2^(n-4))
# - subset #3 gives 1 more unique paths (2^(n-5))
# so that's 2^(n-2)-1 unique paths + 1 for the original = 8
# but now there's one path that's too long (>3) so don't count it (-)
# n=5 means 7 total
#  4 5 6 7 8
#  4 5 6 8
#  4 5 8
# -4 8
#  4 6 8
# x4 8
#  4 5 7 8
# x4 5 8
# x4 8
#  4 7 8
# x4 8
#  4 6 7 8
# x4 6 8
# x4 8
# x4 7 8
# x4 8

# same story with 4 numbers to remove, 4 subsets of 5 numbers
# - subset #1 gives 8 unique paths (2^(n-3))
# - subset #2 gives 4 unique paths (2^(n-4))
# - subset #3 gives 2 more unique paths (2^(n-5))
# - subset #4 gives 1 more unique paths (2^(n-6))
# so that's 2^(n-2)-1 unique paths + 1 for the original = 16
# but now there are 3 paths that are too long - it's the sum of n-4+...+1
# n=6 means 13 total
#  4 5 6 7 8 9
#  4 5 6 7 9
#  4 5 6 9
# -4 5 9
# -4 9
#  4 6 9
# x4 9
#  4 5 7 9
# x4 5 9
# x4 9
#  4 7 9
# x4 9
#  4 6 7 9
# x4 6 9
# x4 9
# x4 7 9
# x4 9

#  4 5 6 8 9
# x4 5 6 9
# x4 5 9
# x4 9
# x4 6 9
# x4 9
#  4 5 8 9
# x4 5 9
# x4 9
# -4 8 9
# x4 9
#  4 6 8 9
# x4 6 9
# x4 9
# x4 8 9
# x4 9

#  4 5 7 8 9
# x4 5 7 9
# x4 5 9
# x4 9
# x4 7 9
# x4 9
# x4 5 8 9
# x4 5 9
# x4 9
# x4 8 9
# x4 9
#  4 7 8 9
# x4 7 9 
# x4 9
# x4 8 9
# x4 9

#  4 6 7 8 9
# x4 6 7 9
# x4 6 9
# x4 9
# x4 7 9
# x4 9
# x4 6 8 9
# x4 6 9
# x4 9
# x4 8 9
# x4 9
# x4 7 8 9
# x4 7 9 
# x4 9
# x4 8 9
# x4 9

# so finally, formula is
#          2^(n-2)-1  [count from all subsets]
#                 +1  [self]
# -(n-4+1)*((n-4)/2)  [count paths too long: (n-4)+(n-5)+...+1]

# 2^(n-2)-(n-3)*((n-4)/2)


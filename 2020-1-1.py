import sys

input = [int(line.strip()) for line in sys.stdin]

# brutal force O(n^2)
for i in range(len(input)):
    for j in range(i+1, len(input)):
        if input[i] + input[j] == 2020:
            print(input[i] * input[j])
            # could break now but let's keep going to see if there are any others

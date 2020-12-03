import sys

input = [int(line.strip()) for line in sys.stdin]

# brutal force O(n^3) but input is small enough it takes <0.5s so I don't care
for i in range(len(input)-2):
    for j in range(i+1, len(input)-1):
        for k in range(j+1, len(input)):
            if input[i] + input[j] + input[k] == 2020:
                print(input[i] * input[j] * input[k])
                # could break now but let's keep going to see if there are any others

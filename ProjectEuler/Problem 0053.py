import math

COMB_FLOOR = int(1e6)
NUMBER_LIMIT = 100

output = 0
for i in range(1, NUMBER_LIMIT + 1):
    for j in range(1, i+1):
        comb = 1
        for k in range(j + 1, i + 1):
            comb *= k
        comb /= math.factorial(i - j)
        if comb > COMB_FLOOR:
            output += 1

print(output)

DIGITS = 10
RANGE = 1000

print(sum([i**i for i in range(1, RANGE + 1)]) % (10 ** DIGITS))

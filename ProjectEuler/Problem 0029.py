LOWER_LIMIT, UPPER_LIMIT = 2, 100

powers = set()
for a in range(LOWER_LIMIT, UPPER_LIMIT + 1):
    for b in range(LOWER_LIMIT, UPPER_LIMIT + 1):
        powers.add(a ** b)

print(len(powers))

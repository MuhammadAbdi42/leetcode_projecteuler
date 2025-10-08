def sum_digits(n: int) -> int:
    return sum(map(lambda x: int(x), str(n)))

maxx = 0
for a in range(1, 100):
    for b in range(1, 100):
        maxx = max(maxx, sum_digits(a ** b))

print(maxx)

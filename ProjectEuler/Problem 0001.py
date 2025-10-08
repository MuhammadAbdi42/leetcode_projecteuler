multiples_3, multiples_5 = set(), set()

i = 3
while i < 1000:
    multiples_3.add(i)
    i += 3

i = 5
while i < 1000:
    multiples_5.add(i)
    i += 5

final_set = multiples_3.union(multiples_5)

print(sum(final_set))

from collections import Counter


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def is_premutation(a: int, b: int) -> bool:
    return Counter(str(a)) == Counter(str(b))


four_digits_primes = []
for i in range(1001, 10000, 2):
    if is_prime(i):
        four_digits_primes.append([i, 0])

prem_groups = []
for i in range(len(four_digits_primes)):
    if four_digits_primes[i][1] == 1:
        continue

    prem = [four_digits_primes[i][0]]
    for j in range(i + 1, len(four_digits_primes)):
        if four_digits_primes[j][1] == 1:
            continue
        if is_premutation(four_digits_primes[i][0], four_digits_primes[j][0]):
            prem.append(four_digits_primes[j][0])
            four_digits_primes[j][1] = 1

    if len(prem) > 1:
        prem_groups.append(prem)

prem_groups = list(filter(lambda x: len(x) >= 3, prem_groups))

for i in range(len(prem_groups)):
    group = prem_groups[i]
    for a in range(0, len(group) - 2):
        first = group[a]
        for b in range(a + 1, len(group) - 1):
            second = group[b]
            for c in range(b+1, len(group)):
                third = group[c]
                if third - second == second - first:
                    print(f'{first}{second}{third}')

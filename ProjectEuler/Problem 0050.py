from typing import List


def sieve(num: int) -> List:
    if num <= 1:
        return []

    numbers = [x for x in range(2, num+1)]

    i = 0
    while i < len(numbers):
        if numbers[i] != 0:
            for j in range(i+numbers[i], len(numbers), numbers[i]):
                numbers[j] = 0
        i += 1

    numbers = list(filter(lambda x: x != 0, numbers))
    return numbers


LIMIT = int(1e6)

primes = sieve(LIMIT)
maxx, maxx_prime = 0, 0
for i in range(len(primes)):
    if primes[i] + primes[i + 1] > LIMIT:
        break

    for j in range(i+1 + (maxx - 1), len(primes)):
        sumx = sum(primes[i:j+1])
        if sumx > LIMIT:
            break

        if sumx in primes and j - i + 1 > maxx:
            maxx = j - i + 1
            maxx_prime = sumx

print(maxx_prime)

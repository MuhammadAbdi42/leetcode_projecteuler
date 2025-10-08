from typing import Dict, List


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


def factors_dict(num: int) -> Dict[int, int]:
    if num < 1:
        return {}
    if num == 1:
        return {1: 1}

    primes = [2]
    factors = {}
    while True:
        power = 0
        while num % primes[-1] == 0:
            num //= primes[-1]
            power += 1

        if power != 0:
            factors[primes[-1]] = power

        if num == 1:
            break

        if primes[-1] == 2:
            i = primes[-1] + 1
        else:
            i = primes[-1] + 2

        while not is_prime(i):
            i += 2
        primes.append(i)

    return factors


def divisors(num: int) -> List[int]:
    if num < 1:
        return []
    if num == 1:
        return [1]

    output = set()
    factors = factors_dict(num)
    if len(factors.keys()) == 1:
        for i in range(factors[list(factors.keys())[0]]+1):
            output.add(list(factors.keys())[0] ** i)
        return sorted(list(output))
    else:
        for i in range(factors[list(factors.keys())[0]]+1):
            multiplier = list(factors.keys())[0] ** i
            rec = divisors(num // (list(factors.keys())
                           [0] ** factors[list(factors.keys())[0]]))
            for j in range(len(rec)):
                rec[j] *= multiplier
                output.add(rec[j])
        return sorted(list(output))


def sum_proper_divisors(num: int) -> int:
    output = 0
    for divisor in divisors(num):
        if divisor == num:
            continue
        output += divisor
    return output


output = 0
seen = set()
for a in range(1, 10000):
    b = sum_proper_divisors(a)
    if a == b:
        continue
    if sum_proper_divisors(b) == a:
        output += a


print(output)

from typing import Dict


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


def triangle_number(n: int) -> int:
    return int(n*(n+1)/2)


def divisors_count(num: int) -> int:
    factors = factors_dict(num)
    count = 1
    for i in factors.values():
        count *= (i + 1)
    return count


LIMIT = 500

i = 1
while True:
    if divisors_count(triangle_number(i)) > LIMIT:
        print(triangle_number(i))
        break
    else:
        i += 1

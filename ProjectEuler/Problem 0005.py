from typing import Dict
import math


primes = [2]


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    if num in primes:
        return True

    for prime in primes:
        if prime > math.sqrt(num):
            break
        if num % prime == 0:
            return False

    if primes[-1] < math.sqrt(num):
        last_checed = len(primes) - 1

        i = primes[-1] + 1
        while i <= math.sqrt(num):
            if (is_prime(i)):
                primes.append(i)
            i += 1

        for i in range(last_checed, len(primes)):
            if num % primes[i] == 0:
                return False

    return True


def prime_factors_list(num) -> Dict[int, int]:
    factors = {}

    if num <= 1:
        return factors

    temp = num
    for i in range(2, num+1):
        if is_prime(i):
            quotient = 0
            while temp % i == 0:
                temp /= i
                quotient += 1
            if quotient:
                factors[i] = quotient

    return factors


common_factors = {}
for i in range(21):
    new_factors = prime_factors_list(i)
    for factor in new_factors.keys():
        if factor not in common_factors:
            common_factors[factor] = new_factors[factor]
        else:
            common_factors[factor] = max(
                common_factors[factor], new_factors[factor])

output = 1
for factor in common_factors:
    output *= int(math.pow(factor, common_factors[factor]))

print(output)

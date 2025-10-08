import math


class Primes:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.primes = self._sieve(limit)

    def _sieve(self, n: int):
        sieve = [True] * (n+1)
        sieve[0] = sieve[1] = False
        for p in range(2, math.isqrt(n) + 1):
            if sieve[p]:
                for multiple in range(p*p, n+1, p):
                    sieve[multiple] = False
        return [p for p in range(2, n+1) if sieve[p]]

    def distinct_factors_count(self, n: int) -> int:
        count = 0
        temp = n
        for p in self.primes:
            if p * p > temp:
                break
            if temp % p == 0:
                count += 1
                while temp % p == 0:
                    temp //= p
        if temp > 1:  # remaining prime factor
            count += 1
        return count


LIMIT = 4

prime_class = Primes(10**6)
factors = [prime_class.distinct_factors_count(x) for x in range(1, LIMIT+1)]

i = 1
while True:
    if factors[i-1:] == [LIMIT] * LIMIT:
        print(i)
        break
    factors.append(prime_class.distinct_factors_count(i + LIMIT))
    i += 1

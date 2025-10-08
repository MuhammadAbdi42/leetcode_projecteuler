from typing import List


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


def rotation_list(num: int) -> List[int]:
    s = str(num)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


TARGET = int(1e6)
circular_primes = set()
seen = set()
for i in range(TARGET):
    if i in seen:
        continue

    if is_prime(i):
        prems = [int(x) for x in rotation_list(i)]
        all_prime = True
        for prem in prems:
            if not is_prime(prem):
                all_prime = False
                break
        if all_prime:
            for prem in prems:
                circular_primes.add(prem)
        for prem in prems:
            seen.add(prem)

print(len(circular_primes))

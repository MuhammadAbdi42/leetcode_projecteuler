TARGET = 10001


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


primes = [2, 3]
i = 5
while len(primes) <= TARGET:
    if is_prime(i):
        primes.append(i)
    i += 2

print(primes[TARGET - 1])

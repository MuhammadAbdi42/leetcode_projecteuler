TARGET = 2e6


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
sum_primes = 5

i = 5
while i < TARGET:
    if is_prime(i):
        primes.append(i)
        sum_primes += i
    i += 2

print(sum_primes)

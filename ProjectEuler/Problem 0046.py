import math


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


i = 9
while True:
    if not is_prime(i):
        found, j = False, 3
        while True:
            if j >= i:
                break

            if is_prime(j):
                diff = int((i - j)/2)
                if diff == math.isqrt(diff) * math.isqrt(diff):
                    found = True
                    break

            j += 2

        if not found:
            print(i)
            break
    i += 2

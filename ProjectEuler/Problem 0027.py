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


RANGE = 1000


def check_quadratic(a: int, b: int) -> int:
    n = 0
    while True:
        num = (n * n) + a * n + b
        if not is_prime(num):
            return n
        n += 1


maxx, A, B = 0, 0, 0
for a in range(-RANGE + 1, RANGE):
    for b in range(1, RANGE + 1):
        if check_quadratic(a, b) > maxx:
            maxx = check_quadratic(a, b)
            A, B = a, b

print(A * B)

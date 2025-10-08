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


def is_truncatable_prime(num: int) -> bool:
    if not is_prime(num) or num < 10:
        return False

    num_s = str(num)
    for i in range(1, len(num_s)):
        r = int(num_s[i:])
        l = int(num_s[:len(num_s) - i])
        if not is_prime(r) or not is_prime(l):
            return False

    return True


LIMIT = 11

valids = []
i = 1
while len(valids) < 11:
    if is_truncatable_prime(i):
        valids.append(i)
    i += 1

print(sum(valids))

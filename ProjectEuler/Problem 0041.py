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


def prem_list(s: str) -> List[str]:
    if len(s) == 1:
        return [s[-1]]

    output = []
    for i in range(len(s)):
        output += list(map(lambda x: s[i] + x, prem_list(s[:i] + s[i+1:])))

    return output


i = 9
found = False
while not found:
    digits = ''.join(str(x) for x in range(1, i+1))
    prems = sorted(prem_list(digits), reverse=True)

    for prem in prems:
        if is_prime(int(prem)):
            print(prem)
            found = True
            break

    i -= 1

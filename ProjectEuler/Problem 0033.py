from collections import Counter
import math


def remove_common_digits(a: int, b: int) -> tuple:
    c1, c2 = Counter(str(a)), Counter(str(b))

    common = c1 & c2
    c1 -= common
    c2 -= common

    a_new = ''.join(ch * c1[ch] for ch in c1)
    b_new = ''.join(ch * c2[ch] for ch in c2)

    if a_new == '':
        a_new = 1
    if b_new == '':
        b_new = 1

    return (int(a_new), int(b_new))


numerator, denominator = 1, 1
for a in range(10, 100):
    for b in range(a+1, 100):
        new_a, new_b = remove_common_digits(a, b)
        if new_b == 0:
            continue

        changed = (new_a != a and new_b != b)
        equal = (a / b == new_a / new_b)
        not_usual = (a % 10 != 0 and b % 10 != 0)

        if changed and equal and not_usual:
            numerator *= a
            denominator *= b

gcd = math.gcd(numerator, denominator)
print(denominator / gcd)

from collections import Counter
from typing import List


def is_premutation(*a) -> bool:
    for i in range(1, len(a)):
        if Counter(str(a[i])) != Counter(str(a[0])):
            return False

    return True

i = 1
while True:
    if is_premutation(2*i, 3*i, 4*i, 5*i, 6*i):
        print(i)
        break
    i += 1


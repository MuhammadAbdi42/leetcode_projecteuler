from typing import List


def has_partition_sum(n: str, target: int) -> bool:
    if int(n) == target:
        return True

    for i in range(1, len(n)):
        l = int(n[:i])
        if has_partition_sum(n[i:], target - l):
            return True

    return False


RANGE = int(1e12)

sumx = 0
i = 4  # The first number that its cube can be divided to 2 or more numbers
while i * i <= RANGE:
    if has_partition_sum(str(i * i), i):
        sumx += i * i
    i += 1

print(sumx)

from typing import List


def prem_list(s: str) -> List[str]:
    if len(s) == 1:
        return [s[-1]]

    output = []
    for i in range(len(s)):
        output += list(map(lambda x: s[i] + x, prem_list(s[:i] + s[i+1:])))

    return output


def substring_divisibility(s: str) -> bool:
    SUBSTRING_DIVISIBILITY = {
        (1, 2, 3): 2,
        (2, 3, 4): 3,
        (3, 4, 5): 5,
        (4, 5, 6): 7,
        (5, 6, 7): 11,
        (6, 7, 8): 13,
        (7, 8, 9): 17
    }

    for substring in SUBSTRING_DIVISIBILITY:
        sub_s = ''
        prime = SUBSTRING_DIVISIBILITY[substring]
        for ind in substring:
            sub_s += s[ind]

        if int(sub_s) % prime != 0:
            return False

    return True


prems = prem_list(''.join(str(x) for x in range(0, 10)))
output = 0
for prem in prems:
    if substring_divisibility(prem):
        output += int(prem)

print(output)

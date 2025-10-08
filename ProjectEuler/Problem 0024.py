from typing import List


def prem_list(s: str) -> List[str]:
    if len(s) == 1:
        return [s[-1]]

    output = []
    for i in range(len(s)):
        output += list(map(lambda x: s[i] + x, prem_list(s[:i] + s[i+1:])))

    return output


TARGET = int(1e6)
prems = prem_list(''.join(str(x) for x in range(0, 10)))
prems.sort()

print(prems[TARGET - 1])

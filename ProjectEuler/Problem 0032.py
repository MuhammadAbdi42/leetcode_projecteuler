from typing import List


def prem_list(s: str) -> List[str]:
    if len(s) == 1:
        return [s[-1]]

    output = []
    for i in range(len(s)):
        output += list(map(lambda x: s[i] + x, prem_list(s[:i] + s[i+1:])))

    return output


valid = set()

digits = ''.join(str(digit) for digit in range(1, 10))
prems = prem_list(digits)

for prem in prems:
    for x in range(1, len(prem) - 1):
        for e in range(x+1, len(prem)):
            multiplicand = int(prem[:x])
            multiplier = int(prem[x:e])
            product = int(prem[e:])

            if multiplicand * multiplier == product:
                valid.add(product)

print(sum(valid))

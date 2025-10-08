# Prime = MULTIPLIER * BASE ^ POWER + REMAINDER
MULTIPLIER = 28433
BASE = 2
POWER = 7830457
REMAINDER = 1

digits = [1] + [0] * 9
# Calculating last 10 digits of BASE ^ POWER
for i in range(POWER):
    for j in range(len(digits)):
        digits[j] *= 2

    for j in range(len(digits)):
        if digits[j] >= 10:
            remainder = digits[j] % 10
            surplus = digits[j] // 10

            digits[j] = remainder
            if j != len(digits) - 1:
                digits[j + 1] += surplus

# Calculating last 10 digits of MULTIPLIER * BASE ^ POWER
for i in range(len(digits)):
    digits[i] *= MULTIPLIER

for i in range(len(digits)):
    if digits[i] >= 10:
        remainder = digits[i] % 10
        surplus = digits[i] // 10

        digits[i] = remainder
        if i != len(digits) - 1:
            digits[i + 1] += surplus

# Caluclating last 10 digits of MULTIPLIER * BASE ^ POWER + REMAINDER
digits[0] += 1
for i in range(len(digits)):
    if digits[i] >= 10:
        remainder = digits[i] % 10
        surplus = digits[i] // 10

        digits[i] = remainder
        if i != len(digits) - 1:
            digits[i + 1] += surplus

digits.reverse()
print(''.join(map(lambda x: str(x), digits)))

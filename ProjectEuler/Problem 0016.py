POWER = 1000

num_digits = [1]

for i in range(POWER):
    for j in range(len(num_digits)):
        num_digits[j] *= 2

    j = 0
    while j < len(num_digits):
        remainder = num_digits[j] // 10
        num_digits[j] = num_digits[j] % 10

        if remainder != 0:
            if j == len(num_digits) - 1:
                num_digits.append(remainder)
            else:
                num_digits[j + 1] += remainder

        j += 1

print(sum(num_digits))

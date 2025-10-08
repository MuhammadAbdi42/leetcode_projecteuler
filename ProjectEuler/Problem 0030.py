POWER = 5

i = 1
output = 0
while True:
    test_bounds = range(10 ** i, 10 ** (i + 1))
    powers_bounds = range(1 ** POWER, (i+1) * (9 ** POWER))

    if test_bounds[0] > powers_bounds[-1]:
        break

    for num in test_bounds:
        sum = 0
        temp = num
        while temp > 0:
            sum += (temp % 10) ** POWER
            temp //= 10
        if num == sum:
            output += num

    i += 1

print(output)

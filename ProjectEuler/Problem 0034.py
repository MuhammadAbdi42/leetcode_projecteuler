import math

i = 1
output = 0
while True:
    test_bounds = range(10 ** i, 10 ** (i + 1))
    upper_bound = (i+1) * math.factorial(9)

    if test_bounds[0] > upper_bound:
        break

    for num in test_bounds:
        sum = 0
        temp = num
        while temp > 0:
            sum += math.factorial(temp % 10)
            temp //= 10
        if num == sum:
            output += num

    i += 1

print(output)

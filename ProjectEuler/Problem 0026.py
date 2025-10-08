def fraction_cycle_length(numerator: int, denominator: int) -> int:
    remainders = {}
    numerator = (numerator % denominator) * 10

    ind = 0
    while numerator != 0:
        remainder = numerator % denominator

        if remainder in remainders:
            return ind - remainders[remainder]
        else:
            remainders[remainder] = ind
            numerator = remainder * 10
            ind += 1

    return 0


num, max_cycle = 0, 0
for i in range(1, 1001):
    if fraction_cycle_length(1, i) > max_cycle:
        num, max_cycle = i, fraction_cycle_length(1, i)

print(num)
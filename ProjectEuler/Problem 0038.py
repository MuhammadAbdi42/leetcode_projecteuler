maxx = 0
i = 1
# The concatenated result must be exactly 9 digits long and formed from at least two products,
# so the base number cannot exceed 4 digits.
while i < 1e4:
    concatenated = ''

    multiplier = 1
    while len(concatenated) < 9:
        concatenated += str(i * multiplier)
        multiplier += 1

    if sorted(concatenated) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if maxx < int(concatenated):
            maxx = int(concatenated)

    i += 1

print(maxx)

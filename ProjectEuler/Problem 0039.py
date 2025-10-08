import math

P = 1000

maxx, max_output = 0, 0
for i in range(P):
    output = 0
    # If we take c as the largest side of the triangle:
    # - By the triangle inequality, c cannot be greater than p/2.
    # - c also cannot be less than (p + 1) / 3, otherwise one of the other sides
    #   would become the largest.
    # → Therefore: (p + 1) / 3 < c < p / 2
    for c in range(math.floor((i+1)/3) + 1, math.ceil(i/2)):
        # If we take b as the second largest side of the triangle:
        # - b must be smaller than c.
        # - For b to be always greater than or equal to a, it should be at least (p - c) / 2.
        # → Therefore: (p - c) / 2 <= b < c
        for b in range(math.ceil((i - c)/2), c):
            a = i - c - b
            if a * a + b * b == c * c:
                output += 1

    if max_output < output:
        max_output = output
        maxx = i

print(maxx)

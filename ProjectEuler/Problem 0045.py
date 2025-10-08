import math


def is_pentagonal_number(n: int) -> bool:
    # Starting with the pentagonal number formula:
    #     P(n) = (1/2) * n * (3n - 1)
    # Rearranging gives:
    #     3n^2 - n - 2P(n) = 0
    # which is quadratic in n.
    #
    # For a positive integer C to be a pentagonal number, the discriminant of this
    # quadratic must be a perfect square:
    #     Δ = 1 + 24C
    # Furthermore, sqrt(Δ) + 1 must be divisible by 6.
    #
    # Solving for n:
    #     n = (1 ± sqrt(1 + 24C)) / 6
    # Since the negative root gives an invalid n, the valid solution is:
    #     n = (1 + sqrt(1 + 24C)) / 6
    if n <= 0:
        return False

    delta = 1 + 24*n
    sqrt_delta = math.isqrt(delta)
    if sqrt_delta * sqrt_delta != delta:
        return False

    return (sqrt_delta + 1) % 6 == 0


def is_hexagonal_number(n: int) -> bool:
    # Starting with the hexagonal number formula:
    #     H(n) = n * (2n - 1)
    # Rearranging gives:
    #     2n^2 - n - H(n) = 0
    # which is quadratic in n.
    #
    # For a positive integer C to be a hexagonal number, the discriminant of this
    # quadratic must be a perfect square:
    #     Δ = 1 + 8C
    # Furthermore, sqrt(Δ) + 1 must be divisible by 4.
    #
    # Solving for n:
    #     n = (1 ± sqrt(1 + 8C)) / 4
    # Since the negative root gives an invalid n, the valid solution is:
    #     n = (1 + sqrt(1 + 8C)) / 4
    if n <= 0:
        return False

    delta = 1 + 8*n
    sqrt_delta = math.isqrt(delta)
    if sqrt_delta * sqrt_delta != delta:
        return False

    return (sqrt_delta + 1) % 4 == 0


def triangle_number(n: int) -> int:
    return int((n*(n + 1))/2)


START_POINT = 286

i = START_POINT
while True:
    num = triangle_number(i)
    if is_pentagonal_number(num) and is_hexagonal_number(num):
        print(num)
        break

    i += 1

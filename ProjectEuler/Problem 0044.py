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


def pentagonal_number(n: int) -> int:
    return int((n*(3*n - 1))/2)


nums = [1]
found = False
while True:
    nums.append(pentagonal_number(len(nums)+1))

    for i in range(0, len(nums) - 1):
        sumx = nums[-1] + nums[i]
        diff = nums[-1] - nums[i]

        if is_pentagonal_number(sumx) and is_pentagonal_number(diff):
            print(diff)
            found = True
            break

    if found:
        break

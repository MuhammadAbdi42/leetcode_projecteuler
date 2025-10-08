import os
import math

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'Files', '0042.txt')
with open(file_path, 'r') as f:
    words = f.read().upper().strip('''"''').split('''","''')
    words.sort()


def word_value(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char) - 64
    return value


def is_triangular_number(n: int) -> bool:
    # For the equation t(n) = (1/2) * n * (n + 1), we can rearrange it as:
    #     n^2 + n - 2t(n) = 0
    # This is a quadratic in n.
    #
    # For a positive nonzero integer C to be a triangular number, the discriminant
    # (Δ = 1 + 8C) must have a square root that is an odd natural number.
    #
    # Solving the quadratic:
    #     n = (1 ± sqrt(1 + 8C)) / 2
    # Since the negative root yields a negative n, the valid solution is:
    #     n = (1 + sqrt(1 + 8C)) / 2
    if n <= 0:
        return False

    delta = 1 + 8*n
    sqrt_delta = math.isqrt(delta)
    if sqrt_delta * sqrt_delta != delta:
        return False

    return sqrt_delta % 2 != 0


output = 0
for word in words:
    if is_triangular_number(word_value(word)):
        output += 1

print(output)

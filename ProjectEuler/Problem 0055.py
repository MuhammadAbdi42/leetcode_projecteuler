def reverse_digits(n: int) -> int:
    return int(str(n)[::-1])


def is_palindrome(a: int) -> bool:
    return str(a) == str(a)[::-1]


NUM_RANGE = int(1e4)
ITERATION_LIMIT = 50

output = 0
for i in range(1, NUM_RANGE):
    iterations = 0
    num = i
    while iterations < ITERATION_LIMIT:
        num += reverse_digits(num)
        iterations += 1

        if is_palindrome(num):
            output += 1
            break

print(NUM_RANGE - 1 - output)

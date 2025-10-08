fibonacci_sequence = [1, 1]

i = 2
while True:
    next_num = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
    if next_num > 4000000:
        break
    else:
        fibonacci_sequence.append(next_num)
        i += 1

fibonacci_sequence = filter(lambda x: x % 2 == 0, fibonacci_sequence)

print(sum(fibonacci_sequence))

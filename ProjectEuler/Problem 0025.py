import copy

TARGET = 1000

fib_1 = [1]
fib_2 = [1]

index = 2
while len(fib_2) < TARGET:
    temp = copy.deepcopy(fib_2)
    for i in range(len(fib_1)):
        fib_2[i] += fib_1[i]
    fib_1 = temp

    i = 0
    while i < len(fib_2):
        remainder = fib_2[i] // 10
        fib_2[i] = fib_2[i] % 10

        if remainder != 0:
            if i == len(fib_2) - 1:
                fib_2.append(remainder)
            else:
                fib_2[i + 1] += remainder

        i += 1

    index += 1

print(index)

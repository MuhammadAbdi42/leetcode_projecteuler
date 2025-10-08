TARGETS = [1, 10, 100, 1000, 10000, 100000, 1000000]

num_string = ''
i = 1
while len(num_string) <= TARGETS[-1]:
    num_string += str(i)
    i += 1

output = 1
for i in range(len(TARGETS)):
    output *= int(num_string[TARGETS[i] - 1])

print(output)

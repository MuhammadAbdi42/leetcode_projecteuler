LIMIT = int(1e6)

output = 0
for i in range(1, LIMIT):
    if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:
        output += i

print(output)

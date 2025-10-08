max = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if str(i*j) == str(i*j)[::-1]:
            if i * j > max:
                max = i * j

print(max)

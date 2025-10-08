SUM_ABC = 1000

a = 1
found = False
while a <= SUM_ABC - 2:
    passed = False
    b = a
    while a + b <= SUM_ABC - 1:
        c = 1000 - a - b
        if c * c == a * a + b * b:
            found = True
            print(a*b*c)
            break
        b += 1
    if found:
        break
    a += 1

GRID_SIZE = 1001

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

shift = 1
max_shift = (GRID_SIZE - 1) // 2
middle = (GRID_SIZE - 1) // 2

pivot = (middle, middle)
grid[pivot[0]][pivot[1]] = 1

i = 2
while shift <= max_shift:
    pivot = (pivot[0], pivot[1] + 1)

    entry = pivot
    se = (middle + shift, middle + shift)
    sw = (middle + shift, middle - shift)
    nw = (middle - shift, middle - shift)
    ne = (middle - shift, middle + shift)

    # From entry to SE corner
    while True:
        grid[pivot[0]][pivot[1]] = i
        i += 1
        pivot = (pivot[0] + 1, pivot[1])

        if pivot == se:
            grid[pivot[0]][pivot[1]] = i
            i += 1
            pivot = (pivot[0], pivot[1] - 1)
            break

    # From SE to SW
    while True:
        grid[pivot[0]][pivot[1]] = i
        i += 1
        pivot = (pivot[0], pivot[1] - 1)

        if pivot == sw:
            grid[pivot[0]][pivot[1]] = i
            i += 1
            pivot = (pivot[0] - 1, pivot[1])
            break

    # From SW to NW
    while True:
        grid[pivot[0]][pivot[1]] = i
        i += 1
        pivot = (pivot[0] - 1, pivot[1])

        if pivot == nw:
            grid[pivot[0]][pivot[1]] = i
            i += 1
            pivot = (pivot[0], pivot[1] + 1)
            break

    # From NW to NE
    while True:

        grid[pivot[0]][pivot[1]] = i
        i += 1
        pivot = (pivot[0], pivot[1] + 1)

        if pivot == ne:
            grid[pivot[0]][pivot[1]] = i
            i += 1
            break

    shift += 1


output = 0
for i in range(GRID_SIZE):
    output += grid[i][i] + grid[GRID_SIZE - 1 - i][i]

output -= grid[middle][middle]

print(output)

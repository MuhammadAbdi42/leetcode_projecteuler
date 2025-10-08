import math

ROWS, COLUMNS = 20, 20

print(math.factorial(ROWS + COLUMNS) /
      (math.factorial(ROWS) * math.factorial(COLUMNS)))

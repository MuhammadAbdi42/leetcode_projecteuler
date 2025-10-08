LIMIT = 100

sum_of_squares = (LIMIT*(LIMIT+1)*((2*LIMIT)+1))/6
square_of_sum = ((LIMIT*(LIMIT+1))/2) ** 2

print(square_of_sum - sum_of_squares)

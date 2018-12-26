def answer(n):
    sum_squares = (n * (n+1) * (2*n+1)) / 6
    square_sums = n**2 * (n+1)**2 / 4
    return square_sums - sum_squares

print(answer(10))
print(answer(100))

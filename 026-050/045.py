from math import sqrt

def triangular(n):
    return sqrt(1 + 8*n) % 2 == 1

def pentagonal(n):
    return sqrt(1 + 24*n) % 6 == 5

n = 144
while True:
    H = 2*n*n - n
    if pentagonal(H) and triangular(H):
        print(H)
        break
    n += 1


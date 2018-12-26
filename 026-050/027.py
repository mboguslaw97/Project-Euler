from helper import prime

maxA, maxB, maxN = 0, 0, 0
for a in range(-999, 1000):
    for b in range(1001):
        n = 0
        while prime(n**2 + a*n + b):
            n += 1
        if n > maxN:
            maxA, maxB, maxN = a, b, n
print(maxA, maxB, maxN)
print(maxA * maxB)

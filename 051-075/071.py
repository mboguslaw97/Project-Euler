q0 = 3 / 7

n1, d1, q1 = 0, 1, 0
n = 1
d = 2
while d <= 1000000:
    d += 1
    while (n + 1) / d < q0:
        n += 1
    if n / d > q1:
        n1, d1, q1 = n, d, n / d
print(n1, d1, q1, q0)

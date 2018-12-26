L = 10 ** 12
x, y = 3, 1
T = 0
while T <= L or not T.is_integer():
    x, y = 3 * x + 8 * y, 3 * y + x
    T = 2 * y + (1 + x) / 2
print(T - y)

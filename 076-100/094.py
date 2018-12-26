from time import time

t0 = time()

total = 0
r1, r2, P = 1, 2, 0
while P < 10 ** 9:
    d = 3 * r1 ** 2 - r2 ** 2
    if d > 0:
        if d < 3:
            x = 2 * r1 ** 2 / d - 1
            P = 6 * x + 2
            total += P
        r2 += 1
    else:
        if d > -3:
            x = -2 * r1 ** 2 / d + 1
            P = 6 * x - 2
            
            total += P
        r1 += 1
print(total - P)

print(time() - t0)

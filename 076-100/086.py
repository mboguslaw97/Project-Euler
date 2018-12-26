from time import time
from math import ceil

t0 = time()

LIMIT = 2000
counts = {M:0 for M in range(3, LIMIT)}
history = set()
y = 1
while (y + 1)**2 - y**2 < LIMIT:
    x = y + 1
    while 2 * x * y < LIMIT or x**2 - y**2 < LIMIT:
        a0, b0 = sorted((2 * x * y, x * x - y * y))
        k = 1
        while k * a0 < LIMIT:
            a1, b1 = k * a0, k * b0
            if (a1, b1) not in history:
                if a1 - ceil(b1 / 2) + 1 > 0:
                    counts[a1] += a1 - ceil(b1 / 2) + 1
                if b1 < LIMIT:
                    counts[b1] += a1 // 2
                history.add((a1, b1))
            k += 1
        x += 1
    y += 1

total = 0
for M in range(3, LIMIT):
    total += counts[M]
    if total > 1000000:
        print(M)
        break
print(total)

print(time() - t0)

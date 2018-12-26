from time import time
from math import sqrt

def gen(n, m = 2):
    yield (n,)
    for x in range(m, int(sqrt(n)) + 1):
        if n % x == 0:
            for group in gen(n // x, x):
                yield group + (x,)

t0 = time()

max_k = 12000
prodsums = {}
p = 4
while len(prodsums) < max_k - 1:
    for group in gen(p):
        l = len(group)
        s = sum(group)
        d = p - s
        k = l + d
        if l > 1 and d >= 0 and k <= max_k and k not in prodsums:
            prodsums[k] = p
    p += 1
print(sum(set(prodsums.values())))

print(time() - t0)

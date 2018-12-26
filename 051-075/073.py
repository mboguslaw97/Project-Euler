from time import time

t0 = time()

LIMIT = 12000
prime_factors = {n : set() for n in range(1, LIMIT)}
for i in range(2, LIMIT):
    if len(prime_factors[i]) == 0:
        for j in range(i, LIMIT, i):
            prime_factors[j].add(i)

result = 0
for d in range(4, LIMIT):
    for n in range(int(d / 3) + 1, int(d / 2) + 1):
        for f in prime_factors[n]:
            if d % f == 0:
                break
        else:
            result += 1
print(result)

print(time() - t0)


from time import time
from math import sqrt
from helper import prime_sieve

t0 = time()

LIMIT = 50000000
primes = tuple(prime_sieve(int(sqrt(LIMIT) + 100)))
sums = set()
i, ival = 0, 4
while True:
    j, jval = 0, 8
    while True:
        k, kval = 0, 16
        while True:
            sums.add(ival + jval + kval)
            k, kval = k + 1, primes[k + 1] ** 4
            if ival + jval + kval >= LIMIT:
                break
        j, jval = j + 1, primes[j + 1] ** 3
        if ival + jval + 16 >= LIMIT:
            break
    i, ival = i + 1, primes[i + 1] ** 2
    if ival + 24 >= LIMIT:
        break 
print(len(sums))

print(time() - t0)

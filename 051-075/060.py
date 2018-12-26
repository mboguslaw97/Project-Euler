from time import time
from helper import prime_sieve, is_prime

def is_concprime(a, b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

def analyze(group, pool):
    if len(group) == 5:
        yield group
        return
    if len(group) + len(pool) < 5:
        return
    for prime in pool:
        yield from analyze(group + [prime], pool & concprimes[prime])

t0 = time()

primes = list(prime_sieve(10000))
concprimes = {}
for i in range(len(primes)):
    concprimes[primes[i]] = set()
    for j in range(i + 1, len(primes)):
        if is_concprime(primes[i], primes[j]):
            concprimes[primes[i]].add(primes[j])

for group in analyze([], set(primes)):
    print(' Group: {}  Sum: {}'.format(group, sum(group)))
        
print(time() - t0)           

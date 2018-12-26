from math import sqrt
from helper import prime_sieve

def is_perm(a, b):
    a_count = {}
    b_count = {}
    for c in str(a):
        a_count[c] = a_count.get(c, 0) + 1
    for c in str(b):
        b_count[c] = b_count.get(c, 0) + 1
    return a_count == b_count

primes = list(prime_sieve(10 ** 4))

result = 2
for i in range(len(primes) - 1, 0, -1):
    for j in range(i + 1, len(primes)):
        pwr = 1
        while primes[i] ** pwr * primes[j] <= 10 ** 7:
            n = primes[i] ** pwr * primes[j]
            while n <= 10 ** 7:
                phi = n - n // primes[i] - n // primes[j] + n // (primes[i] * primes[j])
                quot = n / phi
                if is_perm(n, phi) and quot < result:
                    result = quot
                    print(primes[i], primes[j], n, phi, n / phi)
                n *= primes[j]
            pwr += 1
print(result)

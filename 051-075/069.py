from helper import prime_sieve

primes = prime_sieve(50)
prime = 1

n = 1
while n * prime < 1000000:
    n *= prime
    prime = next(primes)
print(n)

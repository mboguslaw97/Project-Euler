from math import sqrt

primes = [2, 3]

def is_prime(n):
    if n < 2:
        return False
    for x in primes:
        if x >= n:
            return True
        if n % x == 0:
            return False
    for x in range(primes[-1] + 2, int(sqrt(n)) + 2, 2):
        if n % x == 0:
            return False
    return True

def prime_sieve(n):
    nums = [True] * n
    for x in range(2, n):
        if nums[x]:
            if x > primes[-1]:
                primes.append(x)
            yield x
            for i in range(2 * x, n, x):
                nums[i] = False

def prime_factors(n):
    for prime in primes:
        if n % prime == 0:
            yield prime
            while n % prime == 0:
                n //= prime
           
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
            
        
if __name__ == '__main__':
    from time import time
    l1 = [x for x in range(100) if is_prime(x)]
    l2 = list(prime_sieve(100))
    l3 = [x for x in range(100) if is_prime(x)]
    
    print(l1)
    print(l2)
    print(l3)
    print(l1 == l2 == l3)
    

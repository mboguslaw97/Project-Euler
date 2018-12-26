from math import sqrt

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def gen_primes():
    yield 2
    x = 3
    while True:
        for i in range(3, int(sqrt(x))+1, 2):
            if x % i == 0:
                break
        else:
            yield x
        x += 2

def divisors(n):
    k = 1 if n%2==0 else 2
    for i in range(1, int(sqrt(n))+1, k):
        if n % i == 0:
            yield i
            if n//i!=i: yield n // i

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
            
        
if __name__ == '__main__':
    f = fib()
    for i in range(10):
        print(next(f))
    

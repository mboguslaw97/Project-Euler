from math import sqrt

max_prime_test = 3
prime_set = {2, 3}
prime_list = [2, 3]

def prime(n, mode=1):
    if mode == 1:
        global max_prime_test
        if n <= max_prime_test:
            return n in prime_set
        while True:
            max_prime_test += (max_prime_test % 2 == 0)
            for x in range(max_prime_test, n, 2):
                prime(x)
            max_prime_test = n
            lim = int(sqrt(n)) + 1
            for x in prime_list:
                if x > lim:
                    prime_set.add(n)
                    prime_list.append(n)
                    return True
                if n % x == 0:
                    return False
    elif mode == 2:
        for x in prime_set:
            if n % x == 0: return False
        for x in range(prime_list[-1] + 2, int(sqrt(n)) + 2, 2):
            if n % x == 0: return False
        return True

def primes(n=None):
    if n is None:
        yield from prime_list
        x = prime_list[-1] + 2
        while True:
            if prime(x):
                yield x
            x += 2
    else:
        nums = [True] * n
        for x in range(2, n):
            if nums[x]:
                yield x
                for i in range(2 * x, n, x):
                    nums[i] = False

def prime_factors(n):
    while n % 2 == 0:
        yield 2
        n /= 2
    x = 3
    while n > 1:
        if n % x != 0:
            x += 2
        else:
            yield x
            n /= x
            
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
            
        
if __name__ == '__main__':
    from time import time

    print(tuple(prime_factors(33)))
    

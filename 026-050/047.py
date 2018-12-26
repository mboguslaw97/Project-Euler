from time import time
from helper import primes

prime_list = list(primes(999999))
prime_set = set(prime_list)
print('Primes Generated.')

def four_prime_factors(n):
    if n in prime_set:
        count = 1
    else:
        count = 0
        i = 0
        while n > 1:
            if n % prime_list[i] == 0:
                count += 1
                if count > 4:
                    break
                while n % prime_list[i] == 0:
                    n /= prime_list[i]
            i += 1
    return count == 4

t0 = time()
count = 0
x = 1
while count < 4:
    if four_prime_factors(x): count += 1
    else: count = 0
    x += 1
print(x - count) #134043
print(time() - t0)

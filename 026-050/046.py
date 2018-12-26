from math import sqrt, ceil
from helper import primes

prime_set = set(primes(9999))
max_prime = max(prime_set)
x = 7
while x < max_prime:
    x += 2
    if x in prime_set:
        continue
    for y in range(1, ceil(sqrt(x / 2))):
        if x - 2 * y * y in prime_set:
            break
    else:
        print(x)
        break
    

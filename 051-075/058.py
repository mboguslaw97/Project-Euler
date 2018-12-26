from time import time
from helper import is_prime

t0 = time()

prime_count = 0
side_length = 1
x = 1
while True:
    side_length += 2
    for i in range(4):
        x += side_length - 1
        prime_count += is_prime(x)
    if prime_count / (2 * side_length - 1) < .1:
        print(side_length)
        break
print(time() - t0)

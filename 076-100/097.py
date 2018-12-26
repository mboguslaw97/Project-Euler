from time import time

t0 = time()

print((28433 * 2 ** 7830457 + 1) % 10 ** 10)

print(time() - t0)

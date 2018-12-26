from time import time
from math import sqrt

t0 = time()

goal = 2000000
area, min_delta = 0, float('inf')
for w in range(1, 200):
    exp = w * (w + 1)
    h = (sqrt(exp * (exp + 16 * goal)) - exp) // (2 * exp)
    if h < w:
        break
    delta = goal - exp * (h ** 2 + h) / 4
    if delta < min_delta:
        area, min_delta = w * h, delta
    h += 1
    delta = exp * (h ** 2 + h) / 4 - goal
    if delta < min_delta:
        area, min_delta = w * h, delta
        
print(area, min_delta)
print(time() - t0)

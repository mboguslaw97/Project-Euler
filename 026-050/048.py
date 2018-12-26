from time import time
t0 = time()
total = sum(x ** x for x in range(1, 1000))
print(str(total)[-10:])
print(time() - t0)
    

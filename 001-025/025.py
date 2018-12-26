from helper import fib

gen = fib()
lim = 10 ** 999
i = 1
while next(gen) < lim:
    i += 1
print(i)    #4782

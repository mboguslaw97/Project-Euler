from math import factorial as fac

FACS = [fac(x) for x in range(10)]

result = 0
for x in range(10, 3000000):
    if x == sum(FACS[int(c)] for c in str(x)):
        print(x)
        result += x

print(result)

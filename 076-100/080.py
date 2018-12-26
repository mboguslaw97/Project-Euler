from decimal import *

getcontext().prec = 110

result = 0
root = 2
for x in range(2, 100):
    if x == root ** 2:
        root += 1
    else:
        s = str(Decimal(x).sqrt())
        result += int(s[0])
        for i in range(2, 101):
            result += int(s[i])
print(result)

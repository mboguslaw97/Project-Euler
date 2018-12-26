
def period(num, denom):
    remainders = []
    while num > 0:
        if num in remainders:
            return len(remainders) - remainders.index(num)
        remainders.append(num)
        while num < denom:
            num *= 10
        num -= num // denom * denom
    return 0

maxX, maxP = 0, 0
for x in range(2, 1000):
    p = period(1, x)
    if p > maxP:
        maxX, maxP = x, p
print(maxX)

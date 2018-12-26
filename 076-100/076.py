from time import time

##number of ways to add up to n from natural numbers no more than m
def sums(n, m):
    if m == 1:
        return 1
    result = n == m
    for i in range(1, min(n, m + 1)):
        ni, mi = n - i, min(i, n - i, m)
        if (ni, mi) not in saved_sums:
            saved_sums[(ni, mi)] = sums(ni, mi)
        result += saved_sums[(ni, mi)]
    return result

t0 = time()

saved_sums = {}
print(sums(100, 100) - 1) #190569291

print(time() - t0)

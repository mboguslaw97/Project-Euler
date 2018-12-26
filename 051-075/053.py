def nCr(n, r):
    result = 1
    for x in range(r + 1, n + 1):
        result *= x
    for x in range(2, n - r + 1):
        result /= x
    return result

count = 0
for n in range(101):
    for r in range(n):
        if nCr(n, r) > 1000000:
            count += 1
print(count)

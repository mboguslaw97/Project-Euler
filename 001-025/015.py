def answer(n):
    result = 1
    for i in range(1, n+1):
        result *= (n + i) / i
    return result

print(answer(2))
print(answer(20))

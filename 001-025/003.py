def answer(n):
    for i in range(2, n):
        if n % i == 0:
            return answer(n // i)
    return n

print(answer(13195))
print(answer(600851475143))

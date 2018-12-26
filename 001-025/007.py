def answer(n):
    x, count = 1, 1
    while count != n:
        x += 2
        for y in range(3, int(x**.5)+1):
            if x % y == 0:
                break
        else: 
            count += 1
    return x

print(answer(6))
print(answer(10001))

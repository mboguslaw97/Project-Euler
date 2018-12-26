def answer(n):
    x, i = 1, 2
    while True:
        count = 2
        for y in range(2, int(x**.5)+2):
            if x % y == 0:
                count += 2
        if count > n:
            if int(round(x**.5)) == y-1:
                count -= 1
                continue
            return x
        x, i = x+i, i+1
print(answer(500))

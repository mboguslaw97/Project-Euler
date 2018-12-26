def answer(n):
    return sum(int(x) for x in str(n))

print(answer(2**15))
print(answer(2**1000))

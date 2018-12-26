
def answer(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(answer(10))   # 23
print(answer(1000)) # 233168

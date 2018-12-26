
def answer(lim, a=1, b=2, total=0):
    if a > lim: return total
    if a % 2 == 0: total += a
    return answer(lim, b, a+b, total)

print(answer(10))       # 10
print(answer(4000000))  # 4613732
        

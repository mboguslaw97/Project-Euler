def answer(length):
    num = ''
    with open('008.txt') as txt:
        for line in txt:
            num += line.strip()
    m = 1
    for i in range(len(num)-length+1):
        p = 1
        for j in range(i, i+length):
            p *= int(num[j])
        if p > m:
            m = p
    return m

print(answer(4))    # 5832
print(answer(13))   # 23514624000

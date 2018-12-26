def answer(n):
    result = 0
    i = 10**n-1
    while i > 10**(n-1)-1 and i * i > result:
        j = i
        while j > 10**(n-1)-1 and i * j > result:
            if str(i*j) == str(i*j)[::-1]:
                result = i*j
            j -= 1
        i -= 1            
    return result

print(answer(2))
print(answer(3))

from fractions import gcd

def answer(n):
    result = 1
    for i in range(2, n+1):
        if result % i > 0:
            result *= i / gcd(i, result)
    return result    

    
print(answer(10))
print(answer(20))

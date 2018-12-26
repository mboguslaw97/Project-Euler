from math import factorial

def solution(n):
    return sum(int(c) for c in str(factorial(n)))

print(solution(10))     #27
print(solution(100))    #648

def solution(n):
    result = 1
    x = 1
    for i in range(2, n, 2):
        for j in range(4):
            x += i
            result += x
    return result

print(solution(3))      #25
print(solution(5))      #101
print(solution(1001))   #669171001

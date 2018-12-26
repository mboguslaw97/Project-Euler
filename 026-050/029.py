
def solution(a, b):
    terms = set()
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            terms.add(i ** j)
    return len(terms)

print(solution(5, 5))   #15
print(solution(100, 100)) #9183

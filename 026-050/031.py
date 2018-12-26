COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def solution(amt, i=0):
    if amt == 0:
        return 1
    if i == len(COINS):
        return 0
    result = 0
    for count in range(amt // COINS[i] + 1):
        result += solution(amt - count * COINS[i], i + 1)
    return result
        
print(solution(200))

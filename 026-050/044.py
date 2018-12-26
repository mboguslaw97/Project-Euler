def isPentNum(n):
    val = (1 + (1 + 24 * n) ** .5) / 6
    return int(val) == val

pentNums = [i * (3 * i - 1) / 2 for i in range(1, 10000)]
for i in range(len(pentNums)):
    for j in range(i + 1, len(pentNums)):
        pentNum1 = pentNums[i]
        pentNum2 = pentNums[j]
        pentSum = pentNum1 + pentNum2
        pentDif = abs(pentNum1 - pentNum2)
        if isPentNum(pentSum) and isPentNum(pentDif):
            print(pentDif)
            
        

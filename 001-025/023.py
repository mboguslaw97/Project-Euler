from helper import divisors
from time import time

def abundant(n):
    return sum(divisors(n)) - n > n

t0 = time()

result = 0
abundant_list = []
abundant_set = set()
for i in range(1, 28123 + 1):
    if abundant(i):
        abundant_list.append(i)
        abundant_set.add(i)
    j = 0
    while j < len(abundant_list) and abundant_list[j] <= i//2:
        if i - abundant_list[j] in abundant_set: break
        j += 1
    else:
        result += i
print(result)   #4179871

print(time()- t0)

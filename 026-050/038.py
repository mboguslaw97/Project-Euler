def concprod(n):
    cp = ''
    nums = set()
    x = 1
    while True:
        s = str(x * n)
        cp += s
        nums |= set(c for c in s)
        if '0' in nums or len(cp) != len(nums):
            return 0
        if len(cp) >= 9:
            return int(cp)
        x += 1

result = 0
for x in range(10000):
    cp = concprod(x)
    if cp > result:
        result = cp
print(result)

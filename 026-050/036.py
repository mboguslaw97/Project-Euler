def palindromic(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True

result = 0
for x in range(1000000):
    b2, b10 = '{0:b}'.format(x) , str(x)
    if '0' not in [b2[0], b2[-1], b10[0], b10[-1]]:
        if palindromic(b2) and palindromic(b10):
            result += x
print(result)

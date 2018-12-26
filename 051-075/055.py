def palindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[-1-i]:
            return False
    return True

def lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if palindrome(n):
            return False
    return True

count = 0
for x in range(1, 10000):
    if lychrel(x):
        count += 1
print(count)

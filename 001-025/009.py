'''
a^2 + b^2 = c^2
a + b + c = n
c = n - a - b
c^2 = (n - a - b)^2
c^2 = n^2 + a^2 + b^2 + 2ab - 2na - 2nb
a^2 + b^2 = n^2 + a^2 + b^2 + 2ab - 2na - 2nb
0 = n^2 + 2ab - 2na - 2nb
na + nb - ab = (n^2) / 2
'''

def answer(n):
    val = n**2 / 2
    for a in range(1, n-1):
        for b in range(a+1, n):
            if n*a + n*b - a*b == val:
                print(a, b, n-a-b)
                return a * b * (n-a-b)

print(answer(1000))

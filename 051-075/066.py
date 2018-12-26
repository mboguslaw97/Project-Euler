from math import sqrt

result, max_x = 0, 0
root = 2
for D in range(2, 10001):
    if D == root ** 2:
        root += 1
    else:
        s = sqrt(D)
        a0 = int(s)
        a = a0
        P = 1
        Q = a
        n, d = 0, 1
        while (a0 * d + n) ** 2 - D * d ** 2 != 1:            
            a = int(P * (s + Q) / (D - Q ** 2))
            P = (D - Q ** 2) / P
            Q = a * P - Q
            n, d = d, a * d + n
        if a0 * d + n > max_x:
            result, max_x = D, a0 * d + n
print(result, max_x)


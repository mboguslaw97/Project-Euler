from math import sqrt

def period(n):
    s = sqrt(n)
    a = int(s)
    P = 1
    Q = a
    history = set()
    while True:
        a = int(P * (s + Q) / (n - Q ** 2))
        P = (n - Q ** 2) / P
        Q = a * P - Q
        id = (P, Q)
        if id in history:
            return len(history)
        history.add(id)

count = 0
root = 2
for n in range(2, 10001):
    if n == root ** 2:
        root += 1
    else:
        count += period(n) % 2 == 1
print(count)


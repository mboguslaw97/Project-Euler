count = 0
p = 1
n = 1
while True:
    if n ** p >= 10 ** p:
        n = 1
        p += 1
    elif n ** p >= 10 ** (p - 1):
        count += 1
        print(p, count, n ** p)
    n += 1

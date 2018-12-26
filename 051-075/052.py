#contain same digits
def similar(n1, n2):
    s1, s2 = str(n1), str(n2)
    d1, d2 = {}, {}
    for c in s1:
        d1[c] = d1.get(c, 0) + 1
    for c in s2:
        d2[c] = d2.get(c, 0) + 1
    return d1 == d2 

n = 1
while True:
    n += 1
    s = set(str(n))
    for x in range(2, 7):
        if not similar(n, n * x):
            break
    else:
        print(n)
        break

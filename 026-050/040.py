product = 1
k = 1
n = 0
goal = 1
while goal <= 1000000:
    for c in str(k):
        n += 1
        if n == goal:
            print(c)
            product *= int(c)
            goal *= 10
    k += 1
print(product) #210

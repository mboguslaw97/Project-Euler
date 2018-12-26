result = 0
for x in range(2, 1000000):
    if x == sum(int(c) ** 5 for c in str(x)):
        result += x
print(result)   #443839
        

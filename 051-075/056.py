result = 0
for a in range(2, 100):
    for b in range(2, 100):
        result = max(result, sum(int(c) for c in str(a ** b)))
print(result)

count = 0
numer, denom = 1, 2
for i in range(1000):
    if len(str(numer + denom)) > len(str(denom)):
        count += 1
    numer, denom = denom, 2*denom+numer
print(count)

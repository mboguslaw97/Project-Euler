# a + b + c = p
# c = p - a - b
# c^2 = p^2 + a^2 + b^2 + 2ab - 2pa - 2pb

# a^2 + b^2 = c^2
# a^2 + b^2 = p^2 + a^2 + b^2 + 2ab - 2pa - 2pb
# 0 = p^2 + 2ab - 2pa - 2pb
# b = (p^2 - 2pa) / (2p - 2a)

# a <= b < c
# a <= (p^2 - 2pa) / (2p - 2a)
# 2pa - 2a^2 <= p^2 - 2pa
# 4pa <= p^2 + 2a^2

def solutions(p):
    result = 0
    a = 1
    while 4*p*a <= p*p + 2*a*a:
        if (p*p - 2*p*a) % (2*p - 2*a) == 0:
            result += 1
        a += 1
    return result

result, max_sols = 0, 0
for p in range(1, 1001):
    sols = solutions(p)
    if sols > max_sols:
        result, max_sols = p, sols
print(result)
        

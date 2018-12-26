RNs = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
UNITS = [1000, 500, 100, 50, 10, 5, 1]

result = 0
for line in open('089.txt'):
    line = line.strip()
    length = len(line)
    result += length
    
    val = 0
    for i in range(len(line)):
        x = RNs[line[i]]
        if i + 1 < len(line) and x < RNs[line[i + 1]]:
            x *= -1
        val += x

    for unit in UNITS:
        q = val / unit
        if unit in {1, 10, 100} and q >= 4:
            val -= 4 * unit
            result -= 2
        elif unit in {5, 50, 500} and 1.8 <= q < 2.0:
            val -= 1.8 * unit
            result -= 2
        else:
            val -= int(q) * unit
            result -= int(q)
            
print(result)



import string

max_len = 14
trinums = set()

x = 1
trinum = 1
while trinum < 26 * max_len:
    trinums.add(trinum)
    x += 1
    trinum += x

count = 0  
with open('042.txt') as text:
    for line in text:
        for word in line.split(','):
            val = 0
            for i in range(1, len(word) - 1):
                val += string.ascii_uppercase.index(word[i]) + 1
            if val in trinums:
                count += 1
print(count)
            

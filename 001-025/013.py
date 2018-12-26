
total = 0
with open('013.txt') as text:
    for line in text:
        total += int(line)
print(str(total)[:10])

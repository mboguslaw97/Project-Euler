id_creators = {}
id_counts = {}

i = 0
while True:
    i += 1
    cube = i ** 3
    
    id = [0 for i in range(10)]
    for c in str(cube):
        id[int(c)] += 1
    id = tuple(id)
    
    if id not in id_creators:
        id_creators[id] = cube
        id_counts[id] = 0
    id_counts[id] += 1
    
    if id_counts[id] == 5:
        print(id_creators[id])
        break
        

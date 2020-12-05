l1 = []
l2 = []
l3 = []
with open('data/01.txt') as f:
    for line in f:
        line.strip()
        l1.append(int(line))
        l2.append(int(line))
        l3.append(int(line))

for x in l1:
    for y in l2:
        for z in l3:
            if x + y + z == 2020:
                print(x, y, z, x * y * z)
                break

l1 = []
l2 = []
with open('data/01.txt') as f:
    for line in f:
        line.strip()
        l1.append(int(line))
        l2.append(int(line))

for x in l1:
    for y in l2:
        if x + y == 2020:
            print(x, y, x * y)
            break

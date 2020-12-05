l = []
with open('data/05.txt') as f:
    for line in f:
        tmp = line.strip().replace('F','0').replace('B','1').replace('R','1').replace('L','0')
        a, b = tmp[:7], tmp[7:]
        l.append([a, b])

ids = [int(x[0], 2) * 8 + int(x[1], 2) for x in l]
print(max(ids))

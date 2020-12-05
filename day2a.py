l = []
with open('data/02.txt') as f:
    for line in f:
        line = line.replace(':', '').strip().split(' ')
        line[0] = line[0].split('-')
        line[0] = [int(x) for x in line[0]]
        l.append(line)

print(l)

valid = 0

for p in l:
    a = p[0][0]-1
    b = p[0][1]-1
    x = p[2][a]
    y = p[2][b]
    if (p[2][a] == p[1] and p[2][b] != p[1]) or (p[2][a] != p[1] and p[2][b] == p[1]):
        valid += 1

print(valid)

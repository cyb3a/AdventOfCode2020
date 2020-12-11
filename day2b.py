import re

input = []
with open('data/02.txt') as f:
    for line in f:
        line = line.replace(':', '').strip().split(' ')
        line[0] = line[0].split('-')
        line[0] = [int(x) for x in line[0]]
        input.append(line)
valid = 0
for p in input:
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    abc.remove(p[1])
    p[2] = re.sub("|".join(abc), "", p[2])
    if (len(p[2]) >= p[0][0]) & (len(p[2]) <= p[0][1]):
        valid += 1

print(valid)

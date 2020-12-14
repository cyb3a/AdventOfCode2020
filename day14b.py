# looks a lot like https://github.com/arknave/advent-of-code-2020/blob/main/day14/day14.py, but I swear I came up with
# the use of bit shifting and combinations myself.
# "or (a & (1 << i)) > 0" was the missing piece I didn't figure out myself :)
from itertools import combinations
input = open('data/14.txt').read().strip().split('\n')
mem = dict()
for line in input:
    a, b = line.split(" = ")
    if a == "mask":
        current_mask = b
    else:
        a = int(a.replace('mem[', '').replace(']', ''))
        b = int(b)
        v = 0
        possibilities = []
        for i in range(36):
            m = current_mask[-i - 1]
            if m == '1' or (a & (1 << i)) > 0:
                v += (1 << i)
            elif m == 'X':
                possibilities.append(1 << i)
        for j in range(len(possibilities) + 1):
            for com in combinations(possibilities, j):
                mem[v + sum(com)] = b

print(sum(mem.values()))

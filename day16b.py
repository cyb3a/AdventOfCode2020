from pandas.core.common import flatten
from collections import defaultdict

input = open('data/16.txt').read().split('\n\n')
all_rules = [list(map(int, i.split(' ')[-4:])) for i in input[0].replace('or ', '').replace('-', ' ').split('\n')]
rule_names = [i.split(' ')[0] for i in
              input[0].replace('departure ', 'd_').replace('arrival ', 'a_').replace('-', ' ').split('\n')]
my_ticket = list(map(int, input[1].split('\n')[1].split(',')))
tickets = [list(map(int, i.split(','))) + [True] for i in input[2].split('\n')[1:]]
rules = {k: [i for i in range(v[0], v[1] + 1)] + [j for j in range(v[2], v[3] + 1)] for k, v in zip(rule_names, all_rules)}

valids = sorted([i for i in range(min(flatten(all_rules)), max(flatten(all_rules)) + 1)])
valid_tickets = list()
for t in tickets:
    for n in t[:-1]:
        if n not in valids:
            t[-1] = False
    if t[-1]:
        valid_tickets.append(t[:-1])
impossible = defaultdict(list)
possible = defaultdict(list)
definitely = defaultdict(int)
for i in range(len(rules)):
    for t in valid_tickets:
        for rule, includes in rules.items():
            if t[i] not in includes:
                impossible[rule] += [i]

for rule, impossibility in impossible.items():
    possible[rule] = [i for i in range(20) if i not in impossibility]

while True:
    for r, i in possible.items():
        if len(i) == 1:
            definitely[r] = i[0]
            possible.pop(r)
            break
        else:
            for ind, j in enumerate(i):
                if j in definitely.values():
                    i.pop(ind)
                    break
    if len(definitely) == 19:
        break
res = 1
for k, v in definitely.items():
    if str(k).startswith('d_'):
        res *= my_ticket[v]
print(res)

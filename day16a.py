input = open('data/16.txt').read().split('\n\n')
rules = [list(map(int, i.split(' ')[-4:])) for i in input[0].replace('or ', '').replace('-', ' ').split('\n')]
rule_names = [list(map(int, i.split(' ')[-4:])) for i in input[0].replace('or ', '').replace('-', ' ').split('\n')]
my_ticket = list(map(int, input[1].split('\n')[1].split(',')))
tickets = [list(map(int, i.split(','))) for i in input[2].split('\n')[1:]]

valids = []
for r in rules:
    valids += [v for v in range(r[0], r[1]+1)]
    valids += [v for v in range(r[2], r[3]+1)]
valids = list(set(valids))
error_rate = 0
for t in tickets:
    for n in t:
        if n not in valids:
            error_rate += n

print(error_rate)

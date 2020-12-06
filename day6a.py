l = []
with open('data/06.txt') as f:
    l = f.read().split('\n\n')

print(sum([len(set(list(x.replace('\n', '')))) for x in l]))

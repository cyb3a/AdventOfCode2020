from collections import Counter
l = []
with open('data/06.txt') as f:
    l = f.read().split('\n\n')

l = [x.split('\n') for x in l]
summed = 0

for group in l:
    group_size = len(group)
    group_choices = []
    for choice in group:
        group_choices += list(choice)
    for count in Counter(group_choices).values():
        if count == group_size:
            summed += 1

print(summed)

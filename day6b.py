from collections import Counter

input = [x.split('\n') for x in open('data/06.txt').read().split('\n\n')]
summed = 0
for group in input:
    group_size = len(group)
    group_choices = []
    for choice in group:
        group_choices += list(choice)
    for count in Counter(group_choices).values():
        if count == group_size:
            summed += 1

print(summed)

from collections import defaultdict

bag_contains = defaultdict(list)
with open('data/07.txt') as f:
    for line in f:
        t = line.strip().replace('.', '').replace(' contain ', ',').replace('bags', '').replace(' bags', '').replace(
            'bag', '').replace(', ', ',').replace(' ', '').split(',')
        bag_contains[t[0]] = t[1:]
print(bag_contains)


def count_contents(bag):
    print('contens of {}: {}'.format(bag[1:], bag_contains[bag[1:]]))
    if bag_contains[bag[1:]][0] == 'noother':
        return 0
    else:
        return sum([int(b[0]) + int(b[0]) * count_contents(b) for b in bag_contains[bag[1:]]])


print(count_contents('1shinygold'))

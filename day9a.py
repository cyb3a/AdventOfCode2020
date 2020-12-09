from itertools import combinations

with open('data/09.txt') as f:
    input = list(map(int, f.read().split('\n')))

for i, num in enumerate(input):
    if i >= 25:
        c = list(combinations(input[i-25:i], 2))
        c = list(map(lambda x: x[0]+x[1], c))
        if num not in c:
            print(num)

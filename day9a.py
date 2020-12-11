from itertools import combinations

input = list(map(int, open('data/09.txt').read().split('\n')))
for i, num in enumerate(input):
    if i >= 25 and num not in list(map(lambda x: x[0]+x[1], list(combinations(input[i-25:i], 2)))):
        print(num)

from itertools import combinations

input = list(map(int, open('data/09.txt').read().split('\n')))
corrupted_num = 0
for i, num in enumerate(input):
    if i >= 25:
        if num not in list(map(lambda x: x[0] + x[1], list(combinations(input[i - 25:i], 2)))):
            corrupted_num = num
for i, num in enumerate(input):
    j = i
    while num <= corrupted_num:
        num += input[j + 1]
        j += 1
        if num == corrupted_num:
            print(max(input[i:j+1]) + min(input[i:j+1]))

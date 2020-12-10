with open('data/10.txt') as f:
    input = sorted(list(map(int, f.read().split('\n'))))

input.append(0)
input.append(max(input)+3)
threes = 1
ones = 1

for i, num in enumerate(input[:-1]):
    if input[i + 1] - num == 1:
        ones += 1
    elif input[i + 1] - num == 3:
        threes += 1

print(threes * ones)

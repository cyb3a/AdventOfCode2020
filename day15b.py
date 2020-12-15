from collections import defaultdict

numbers = [0, 13, 1, 16, 6, 17]
counts = defaultdict(int)
last_index = defaultdict(int)
for i, num in enumerate(numbers):
    counts[num] = 1
    last_index[num] = i+1
for i in range(30000000 - len(numbers)):
    if counts[numbers[-1]] == 1:
        num = 0
        last_index[numbers[-1]] = len(numbers)
    elif counts[numbers[-1]] > 1:
        num = len(numbers) - last_index[numbers[-1]]
        last_index[numbers[-1]] = len(numbers)
    else:
        num = 0
    numbers.append(num)
    counts[num] += 1

print(numbers[-1])

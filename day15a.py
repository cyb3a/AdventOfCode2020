from collections import defaultdict

numbers = [0, 13, 1, 16, 6, 17]
counts = defaultdict(int)
for num in numbers:
    counts[num] = 1
for i in range(2020 - len(numbers)):
    if counts[numbers[-1]] > 1:
        ind = [index + 1 for index, v in enumerate(numbers) if v == numbers[-1]]
        num = ind[-1] - ind[-2]
    else:
        num = 0
    numbers.append(num)
    counts[num] += 1

print(numbers[-1])

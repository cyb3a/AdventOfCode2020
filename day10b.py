with open('data/10.txt') as f:
    input = sorted(list(map(int, f.read().split('\n'))))

input.append(max(input) + 3)
last_num = 0
tmp = 0
possibilities = 0
dp = [0] * len(input)
diff = []

for i, num in enumerate(input):
    diff.append(num - last_num)
    while tmp < i and input[tmp] < num - 3:
        possibilities -= dp[tmp]
        tmp += 1
    dp[i] = possibilities + (num <= 3)
    possibilities += dp[i]
    last_num = num

print(dp[-1])

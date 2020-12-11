input = [int(line.strip()) for line in open('data/01.txt')]
for x in input:
    for y in input:
        if x + y == 2020:
            print(x * y)

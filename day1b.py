input = [int(line.strip()) for line in open('data/01.txt')]
for x in input:
    for y in input:
        for z in input:
            if x + y + z == 2020:
                print(x * y * z)

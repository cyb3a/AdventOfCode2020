from collections import defaultdict

input = open('data/17.txt').read().split('\n')
grid = defaultdict(bool)


def check_energy(grid):
    tmp = {}
    for x in range(min(k[0] for k in grid.keys()) - 1, max(k[0] for k in grid.keys()) + 2):
        for y in range(min(k[1] for k in grid.keys()) - 1, max(k[1] for k in grid.keys()) + 2):
            for z in range(min(k[2] for k in grid.keys()) - 1, max(k[2] for k in grid.keys()) + 2):
                current_activity = grid.get((x, y, z), False)
                cnt_active_neighbours = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        for dz in (-1, 0, 1):
                            if dx == dy == dz == 0:
                                continue
                            elif grid.get((x + dx, y + dy, z + dz), False):
                                cnt_active_neighbours += 1
                if (current_activity and cnt_active_neighbours in (2, 3)) or (
                        not current_activity and cnt_active_neighbours == 3):
                    tmp[(x, y, z)] = True
    return tmp


for row, line in enumerate(input):
    for col, char in enumerate(line):
        grid[(row, col, 0)] = char == '#'

for i in range(6):
    grid = check_energy(grid)
print(sum(grid.values()))

import numpy as np

def split_val(x):
    a, b = x[0], int(x[1:])
    if a == 'R':
        if b == 90:
            a, b = 'L', 270
        elif b == 180:
            a = 'L'
        elif b == 270:
            a, b = 'L', 90
    return a, b


def move(direction, instruction):
    if direction == 'S':
        return coordinates[0], coordinates[1] - instruction
    elif direction == 'N':
        return coordinates[0], coordinates[1] + instruction
    elif direction == 'W':
        return coordinates[0] - instruction, coordinates[1]
    elif direction == 'E':
        return coordinates[0] + instruction, coordinates[1]


input = list(map(split_val, open('data/12.txt').read().split('\n')))
coordinates = (0, 0)
current_direction = 'E'

for direction, instruction in input:
    if direction in ['S', 'N', 'W', 'E']:
        coordinates = move(direction, instruction)
    elif direction == 'F':
        coordinates = move(current_direction, instruction)
    elif direction == 'L':
        if instruction == 180:
            if current_direction == 'N':
                current_direction = 'S'
            elif current_direction == 'S':
                current_direction = 'N'
            elif current_direction == 'W':
                current_direction = 'E'
            elif current_direction == 'E':
                current_direction = 'W'
        elif instruction == 90:
            if current_direction == 'N':
                current_direction = 'W'
            elif current_direction == 'S':
                current_direction = 'E'
            elif current_direction == 'W':
                current_direction = 'S'
            elif current_direction == 'E':
                current_direction = 'N'
        elif instruction == 270:
            if current_direction == 'N':
                current_direction = 'E'
            elif current_direction == 'S':
                current_direction = 'W'
            elif current_direction == 'W':
                current_direction = 'N'
            elif current_direction == 'E':
                current_direction = 'S'


print(np.abs(coordinates[0]) + np.abs(coordinates[1]))

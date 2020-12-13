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


def move_wp(direction, instruction):
    if direction == 'S':
        return waypoint[0], waypoint[1] - instruction
    elif direction == 'N':
        return waypoint[0], waypoint[1] + instruction
    elif direction == 'W':
        return waypoint[0] - instruction, waypoint[1]
    elif direction == 'E':
        return waypoint[0] + instruction, waypoint[1]


input = list(map(split_val, open('data/12.txt').read().split('\n')))
coordinates = (0, 0)
waypoint = (10, 1)
for direction, instruction in input:
    if direction in 'SNWE':
        waypoint = move_wp(direction, instruction)
    elif direction == 'F':
        coordinates = coordinates[0] + waypoint[0] * instruction, coordinates[1] + waypoint[1] * instruction
    elif direction == 'L':
        while instruction > 0:
            waypoint = - waypoint[1], waypoint[0]
            instruction -= 90

print(np.abs(coordinates[0]) + np.abs(coordinates[1]))

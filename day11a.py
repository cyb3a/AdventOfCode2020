input = [['.'] + list(x) + ['.'] for x in open('data/11.txt').read().split('\n')]
input = [['.'] * len(input[0])] + input + [['.'] * len(input[0])]


def check_adjacent(i, j):
    near_seats_count = 0
    # check above:
    if input[i - 1][j - 1] == '#':
        near_seats_count += 1
    if input[i - 1][j] == '#':
        near_seats_count += 1
    if input[i - 1][j + 1] == '#':
        near_seats_count += 1
    # check below
    if input[i + 1][j - 1] == '#':
        near_seats_count += 1
    if input[i + 1][j] == '#':
        near_seats_count += 1
    if input[i + 1][j + 1] == '#':
        near_seats_count += 1
    # check left and right
    if input[i][j - 1] == '#':
        near_seats_count += 1
    if input[i][j + 1] == '#':
        near_seats_count += 1
    # change status
    if input[i][j] == 'L' and near_seats_count == 0:
        to_change[i][j] = True
    elif input[i][j] == '#' and near_seats_count >= 4:
        to_change[i][j] = True


def change_seats(i, j):
    if to_change[i][j]:
        input[i][j] = 'L' if input[i][j] == '#' else '#'


def reset_to_change():
    return [[False for j in range(len(input[0]))] for i in range(len(input))]


def count_occupied():
    return ''.join([''.join(x) for x in input]).count('#')


old_cnt = count_occupied()
to_change = reset_to_change()
new_cnt = 1

while old_cnt != new_cnt:
    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            check_adjacent(i, j)
    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            change_seats(i, j)
    to_change = reset_to_change()
    old_cnt = new_cnt
    new_cnt = count_occupied()

print(new_cnt)

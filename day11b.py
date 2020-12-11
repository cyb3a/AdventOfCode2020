input = [['X'] + list(x) + ['X'] for x in open('data/11.txt').read().split('\n')]
input = [['X'] * len(input[0])] + input + [['X'] * len(input[0])]


def check_above_left(i, j):
    return input[i - 1][j - 1] if input[i - 1][j - 1] != '.' else check_above_left(i - 1, j - 1)


def check_above(i, j):
    return input[i - 1][j] if input[i - 1][j] != '.' else check_above(i - 1, j)


def check_above_right(i, j):
    return input[i - 1][j + 1] if input[i - 1][j + 1] != '.' else check_above_right(i - 1, j + 1)


def check_below_left(i, j):
    return input[i + 1][j - 1] if input[i + 1][j - 1] != '.' else check_below_left(i + 1, j - 1)


def check_below(i, j):
    return input[i + 1][j] if input[i + 1][j] != '.' else check_below(i + 1, j)


def check_below_right(i, j):
    return input[i + 1][j + 1] if input[i + 1][j + 1] != '.' else check_below_right(i + 1, j + 1)


def check_left(i, j):
    return input[i][j - 1] if input[i][j - 1] != '.' else check_left(i, j - 1)


def check_right(i, j):
    return input[i][j + 1] if input[i][j + 1] != '.' else check_right(i, j + 1)


def check_adjacent(i, j):
    near_seats_count = 0
    if check_above_left(i, j) == '#':
        near_seats_count += 1
    if check_above(i, j) == '#':
        near_seats_count += 1
    if check_above_right(i, j) == '#':
        near_seats_count += 1
    if check_below_left(i, j) == '#':
        near_seats_count += 1
    if check_below(i, j) == '#':
        near_seats_count += 1
    if check_below_right(i, j) == '#':
        near_seats_count += 1
    if check_left(i, j) == '#':
        near_seats_count += 1
    if check_right(i, j) == '#':
        near_seats_count += 1
    if input[i][j] == 'L' and near_seats_count == 0:
        to_change[i][j] = True
    elif input[i][j] == '#' and near_seats_count >= 5:
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
    for i in range(len(input) - 1):
        for j in range(len(input[0]) - 1):
            if input[i][j] != 'X' and input != '.':
                check_adjacent(i, j)
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] in ['#', 'L']:
                change_seats(i, j)
    to_change = reset_to_change()
    old_cnt = new_cnt
    new_cnt = count_occupied()

print(new_cnt)

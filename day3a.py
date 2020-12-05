import numpy as np

l1 = []
with open('data/03.txt') as f:
    for line in f:
        l1.append(list(line.strip() * 100))


# need to go down 323 steps

def tree_counting(right, down):
    row = 0
    col = 0
    tree_counter = 0
    while row < len(l1) - 1:
        col += right
        row += down
        if l1[row][col] == '#':
            tree_counter += 1
            l1[row][col] = 'X'
            print(row, col, l1[row][col])
        else:
            l1[row][col] = 'O'
            print(row, col, l1[row][col])
    return tree_counter


print((tree_counting(3, 1)))

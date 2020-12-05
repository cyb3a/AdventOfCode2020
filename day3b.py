import numpy as np
l1 = []
with open('data/03.txt') as f:
    for line in f:
        l1.append(list(line.strip()*100))

# need to go down 323 steps

def tree_counting(right, down):
    row = 0
    col = 0
    tree_counter = 0
    while row < len(l1)-1:
        col += right
        row += down
        if l1[row][col] == '#':
            tree_counter += 1
            l1[row][col] = 'X'
            #print(row, col, l1[row][col])
        else:
            l1[row][col] = 'O'
            #print(row, col, l1[row][col])
    return tree_counter

tree_count = []

tree_count.append(tree_counting(1, 1))
tree_count.append(tree_counting(3, 1))
tree_count.append(tree_counting(5, 1))
tree_count.append(tree_counting(7, 1))
tree_count.append(tree_counting(1, 2))

m = tree_count[0] * tree_count[1] * tree_count[2] * tree_count[3] * tree_count[4]
print(m)
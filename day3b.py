input = [list(line.strip() * 100) for line in open('data/03.txt')]


def tree_counting(right, down):
    row = col = tree_counter = 0
    while row < len(input) - 1:
        col += right
        row += down
        if input[row][col] == '#':
            tree_counter += 1
            input[row][col] = 'X'
        else:
            input[row][col] = 'O'
    return tree_counter


print(tree_counting(1, 1) * tree_counting(3, 1) * tree_counting(5, 1) * tree_counting(7, 1) * tree_counting(1, 2))

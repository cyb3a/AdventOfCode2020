input = [list(line.strip() * 100) for line in open('data/03.txt')]


def tree_counting(right, down):
    row = col = tree_counter = 0
    while row < len(input) - 1:
        col += right
        row += down
        if input[row][col] == '#':
            tree_counter += 1
            input[row][col] = 'X'
            print(row, col, input[row][col])
        else:
            input[row][col] = 'O'
            print(row, col, input[row][col])
    return tree_counter


print(tree_counting(3, 1))

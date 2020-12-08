code = []
with open('data/08.txt') as f:
    for i, line in enumerate(f):
        instruction, num = line.strip().split(' ')
        code.append([i, instruction, num[0], int(num[1:]), False])


def read_line(line, accumulator=0):
    if line[4]:
        print(accumulator)
    else:
        line[4] = True
        if line[1] == 'jmp' and line[2] == '+':
            read_line(code[line[0] + line[3]], accumulator)
        elif line[1] == 'jmp' and line[2] == '-':
            read_line(code[line[0] - line[3]], accumulator)
        elif line[1] == 'acc' and line[2] == '+':
            accumulator += line[3]
            read_line(code[line[0] + 1], accumulator)
        elif line[1] == 'acc' and line[2] == '-':
            accumulator -= line[3]
            read_line(code[line[0] + 1], accumulator)
        else:
            read_line(code[line[0] + 1], accumulator)


read_line(code[0])

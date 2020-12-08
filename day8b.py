def read_code():
    code = []
    with open('data/08.txt') as f:
        for i, line in enumerate(f):
            instruction, num = line.strip().split(' ')
            code.append([i, instruction, num[0], int(num[1:])])
    return code


def read_line(line, steps=0, accumulator=0, seen=[]):
    steps += 1
    try:
        if line[0] in seen:
            return 0
        else:
            seen.append(line[0])
            if line[1] == 'jmp' and line[2] == '+':
                read_line(code[line[0] + line[3]], steps, accumulator, seen)
            elif line[1] == 'jmp' and line[2] == '-':
                read_line(code[line[0] - line[3]], steps, accumulator, seen)
            elif line[1] == 'acc' and line[2] == '+':
                accumulator += line[3]
                read_line(code[line[0] + 1], steps, accumulator, seen)
            elif line[1] == 'acc' and line[2] == '-':
                accumulator -= line[3]
                read_line(code[line[0] + 1], steps, accumulator, seen)
            else:
                read_line(code[line[0] + 1], steps, accumulator, seen)
    except IndexError:
        print('Line is {} and current accumulator is {}.'.format(line, accumulator))


def swap_jmp_nop(line):
    if line[1] == 'jmp':
        line[1] = 'nop'
        return line
    elif line[1] == 'nop':
        line[1] = 'jmp'
        return line
    else:
        return line


counter = 0
while counter < len(read_code()):
    code = read_code()
    code[counter] = swap_jmp_nop(code[counter])
    read_line(code[0], seen=[])
    code[counter][0] = swap_jmp_nop(code[counter])
    counter += 1

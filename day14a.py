input = open('data/14.txt').read().split('\n')
mem = dict()
current_mask = list('X'*36)
for line in input:
    if line.startswith('mask'):
        current_mask = list(line.split('= ')[1])
        print(current_mask)
    else:
        addr, val = line.replace('mem[', '').replace(']', '').split(' = ')
        val = list(str(bin(int(val)))[2:])
        p = 36-len(val)
        val = list('0'*p) + val
        for i in range(36):
            if current_mask[i] == '0':
                val[i] = '0'
            elif current_mask[i] == '1':
                val[i] = '1'
        mem[addr] = int(''.join(val), 2)

print(sum(mem.values()))

import re
hcl_pattern = '^#[a-f0-9]{6}$'
pid_pattern = '^[0-9]{9}$'

l = list()
with open('data/04.txt') as f:
    l = f.read().split('\n\n')

passports_count = 0
for p in l:
    pp = p.replace('\n', ' ').split(' ')
    if len(pp) == 8 or (len(pp) == 7 and 'cid' not in ''.join(pp)):
        is_valid = True
        for f in pp:
            k, v = f.split(':')
            if k == 'byr':
                if len(v) != 4 or int(v) < 1920 or int(v) > 2002:
                    is_valid = False
                    pass
            if k == 'iyr':
                if len(v) != 4 or int(v) < 2010 or int(v) > 2020:
                    is_valid = False
                    pass
            if k == 'eyr':
                if len(v) != 4 or int(v) < 2020 or int(v) > 2030:
                    is_valid = False
                    pass
            if k == 'hgt':
                if v[-2:] != 'cm' and v[-2:] != 'in':
                    is_valid = False
                    pass
                else:
                    unit = v[-2:]
                    v = int(v[:-2])
                    if (unit == 'cm' and (v < 150 or v > 193)) or (unit == 'in' and (v < 59 or v > 76)):
                        is_valid = False
                        pass
            if k == 'hcl':
                if not re.match(hcl_pattern, v):
                    is_valid = False
                    pass
            if k == 'ecl':
                if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    is_valid = False
                    pass
            if k == 'pid':
                if not re.match(pid_pattern, v):
                    is_valid = False
                    pass
        if is_valid:
            passports_count += 1

print(passports_count)

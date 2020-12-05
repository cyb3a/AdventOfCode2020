l = []
with open('data/04.txt') as f:
    l = f.read().split('\n\n')

passports = 0
for p in l:
    pp = p.replace('\n', ' ').split(' ')
    if len(pp) == 8 or (len(pp) == 7 and 'cid' not in ''.join(pp)):
        passports += 1

print(passports)

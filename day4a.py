passports = 0
for p in open('data/04.txt').read().split('\n\n'):
    pp = p.replace('\n', ' ').split(' ')
    if len(pp) == 8 or (len(pp) == 7 and 'cid' not in ''.join(pp)):
        passports += 1

print(passports)

from collections import Counter

input = [line.split(' (contains ') for line in open('data/21.txt').read().split('\n')]

allergens = {}
cnt = Counter()
for ing, ale in input:
    ing = set(ing.split())
    ale = ale[:-1].split(', ')
    for a in ale:
        if a not in allergens:
            allergens[a] = ing
        else:
            allergens[a] &= ing
    cnt.update(ing)
for a in allergens:
    for w in allergens[a]:
        cnt.pop(w) if w in cnt else None

for a, i in allergens.items():
    print(a, i)

# yes, I did the following by hand from above output :shrug:
definitive = {'wheat': 'qsjszn', 'soy': 'cpxmpc', 'shellfish': 'qnvx', 'dairy': 'cljf', 'fish': 'vvfjj',
              'nuts': 'qmrps', 'eggs': 'frtfg', 'peanuts': 'hvnkk'}

res = ''
for a, i in sorted(definitive.items()):
    res += i+','
print(res)

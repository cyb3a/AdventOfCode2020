from pandas.core.common import flatten


def remove(digit_list):
    digit_list = [''.join(x for x in i if x.isalpha()) for i in digit_list]
    return digit_list


def can_contain_gold(bag):
    if all_contents[bag][0] == 'noother':
        return 'n'
    else:
        if 'shinygold' in ''.join(all_contents[bag]):
            return 'y'
        else:
            return [can_contain_gold(b) for b in all_contents[bag]]


all_contents = {}
shiny_gold_content = {}
with open('data/07.txt') as f:
    for line in f:
        t = remove(
            line.strip().replace('.', '').replace(' contain ', ',').replace('bags', '').replace(' bags', '').replace(
                'bag', '').replace(', ', ',').split(','))
        all_contents[t[0]] = t[1:]

for bag in all_contents.keys():
    shiny_gold_content[bag] = list(flatten(can_contain_gold(bag)))

has_shiny_gold = 0
for bag in shiny_gold_content.keys():
    if 'y' in shiny_gold_content[bag]:
        has_shiny_gold += 1

print(has_shiny_gold)

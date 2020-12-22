rules, messages = open('data/19.txt').read().replace('"', '').split('\n\n')
rules = rules.split('\n')
messages = messages.split('\n')

print(messages)
print(rules)
rules = {r.split(': ')[0]: r.split(': ')[1].split(' | ') for r in rules}
print(rules)
print(rules['39'], rules['0'])
for ru in rules['0']:
    for r in ru.split():
        print(rules[r])


def
print(sum([len(set(list(x.replace('\n', '')))) for x in open('data/06.txt').read().split('\n\n')]))

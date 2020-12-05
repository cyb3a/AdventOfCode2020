boarding_passes = []
with open('data/05.txt') as f:
    for line in f:
        boarding_passes.append(line.strip().replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'))

ids = [int(x, 2) for x in boarding_passes]
ids = sorted(ids)

for i in range(len(ids[:-1])):
    if ids[i] + 1 != ids[i + 1]:
        print('Seat left: {}\nSeat right: {}\nMy seat: {}'.format(ids[i], ids[i + 1], ids[i] + 1))

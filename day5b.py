boarding_passes = sorted(
    [int(line.strip().replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'), 2) for line in
     open('data/05.txt')])
for i in range(len(boarding_passes[:-1])):
    if boarding_passes[i] + 1 != boarding_passes[i + 1]:
        print('Seat left: {}\nSeat right: {}\nMy seat: {}'.format(boarding_passes[i], boarding_passes[i + 1],
                                                                  boarding_passes[i] + 1))

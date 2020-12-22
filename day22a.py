_, player1, _, player2 = [f.split('\n') for f in open('data/22.txt').read().replace('\n\n',':').split(':')]
player1 = list(map(int, player1[1:]))
player2 = list(map(int, player2[1:]))

while player1 and player2:
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    if p1 > p2:
        player1 += [p1, p2]
    else:
        player2 += [p2, p1]

winner = player1 if len(player1) > 0 else player2
print(sum(i * card for i, card in enumerate(reversed(winner), 1)))

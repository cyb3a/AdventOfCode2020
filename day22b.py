_, player1, _, player2 = [f.split('\n') for f in open('data/22.txt').read().replace('\n\n',':').split(':')]
player1 = list(map(int, player1[1:]))
player2 = list(map(int, player2[1:]))


def recursive_combat(pl1, pl2):
    past_hands = set()
    while len(pl1) > 0 and len(pl2) > 0:
        current_hands = (tuple(pl1), tuple(pl2))
        if current_hands in past_hands:
            return 1, pl1, pl2
        else:
            past_hands.add(current_hands)
        p1 = pl1[0]
        p2 = pl2[0]
        if len(pl1) > p1 and len(pl2) > p2:
            win, *_ = recursive_combat(pl1[1:p1 + 1], pl2[1:p2 + 1])
        elif p1 > p2:
            win = 1
        else:
            win = 2

        if win == 1:
            pl1 = pl1[1:] + [p1, p2]
            pl2 = pl2[1:]
        else:
            pl1 = pl1[1:]
            pl2 = pl2[1:] + [p2, p1]

    return 1 if pl1 else 2, pl1, pl2


_, p1, p2 = recursive_combat(player1, player2)
winner = p1 if p1 else p2
print(sum(i * card for i, card in enumerate(reversed(winner), 1)))

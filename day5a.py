print(max([int(x, 2) for x in
           [line.strip().replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0') for line in
            open('data/05.txt')]]))

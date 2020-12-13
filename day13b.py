# most credit goes to https://github.com/lelilia/ <3
busses = [(x[0], int(x[1])) for x in enumerate(open('data/13.txt').read().split('\n')[1].split(',')) if x[1] != 'x']
t = 0
stepsize = 1
print(busses)
for departure, bus in busses:
    while t % bus != (bus - departure) % bus:
        t += stepsize
    stepsize *= bus
print(t)

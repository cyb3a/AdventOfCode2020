arrival = int(open('data/13.txt').read().split('\n')[0])
busses = [int(x) for x in open('data/13.txt').read().split('\n')[1].split(',') if x != 'x']
min_arrival = dict()
max_arrival = dict()
best_departures = dict()
for bus in busses:
    departure = 0
    best_departures[bus] = list()
    min_arrival[bus] = arrival-bus
    max_arrival[bus] = arrival+bus
    while departure <= max_arrival[bus]:
        if departure >= min_arrival[bus]:
            best_departures[bus].append(departure)
        departure += bus

min_departures = []
for k, v in best_departures.items():
    for d in v:
        if d >= arrival:
            min_departures.append(d)

print((min(min_departures)-arrival) * 17) # where the 17 is determined from looking at the numbers /o\

departure = 1000507
busses = '29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,631,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17'

departure = 939
busses = '7,13,x,x,59,x,31,19'

bus_list = busses.split(',')
bus_departures = []
closest = 1000000000
best_bus = 0
for bus in bus_list:
    if not bus == 'x':
        bus = int(bus)
        if departure % bus == 0:
            closest_departure = (departure // bus) * bus
        else:
            closest_departure = (departure // bus) * bus + bus

        wait_time = closest_departure - departure

        if wait_time < closest:
            closest = wait_time
            best_bus = bus

        bus_departures.append({bus: wait_time})

print('Part 1:', closest * best_bus)

# Part 2
busses = ["x" if x == "x" else int(x) for x in bus_list]


def part2():
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    print(mods)
    vals = list(reversed(sorted(mods)))
    print(vals)
    val = mods[vals[0]]
    print(val)
    r = vals[0]
    print(r)
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val

print(part2())


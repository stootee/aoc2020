from inputs import rules, nearby_tickets, your_ticket
from numpy import array, prod

acceptable_values = set()

for k, v in rules.items():
    key_range = set()
    for ranges in v.split(' or '):
        range_start, range_end = ranges.split('-')
        this_range = range(int(range_start), int(range_end) + 1)
        key_range.update(this_range)

        acceptable_values.update(this_range)

    rules[k] = key_range

nearby_ticket_list = []
for ticket in nearby_tickets.splitlines():
    tkt = []
    for values in ticket.split(','):
        tkt.append(int(values))
    nearby_ticket_list.append(tkt)

valid_tickets = []
invalid_values = []
for x in nearby_ticket_list:
    inv = list(set(x).difference(acceptable_values))
    if inv:
        invalid_values += inv
    else:
        valid_tickets.append(x)

print('Part1:', sum(invalid_values))

arr = array(valid_tickets).transpose()

rule_map = {}
while len(rule_map) < len(rules):
    for n, x in enumerate(arr):
        if n not in rule_map.values():
            possibles = []
            for k, v in [(k, v) for k, v in rules.items() if k not in rule_map.keys()]:

                could_be = set(x).difference(v)
                if len(could_be) == 0:
                    possibles.append(k)

            if len(possibles) == 1:
                print(f'col {n} can only be {possibles[0]}')
                rule_map[possibles[0]] = n

print(prod(list([your_ticket[i] for i in [v for k, v in rule_map.items() if k[:9] == 'departure']])))

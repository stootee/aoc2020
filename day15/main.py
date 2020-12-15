spoken = [17, 1, 3, 16, 19, 0]
turns = 30000000

for turn in range(len(spoken), 2021):
    nekops = list(reversed(spoken))
    last_spoken = nekops[0]

    if spoken.count(last_spoken) == 1:
        spoken.append(0)
    else:
        last_but_one = len(nekops) - nekops[1:].index(last_spoken) -1

        spoken.append(len(nekops) - last_but_one)

print(spoken[2019])

###

spoken = {17: 1, 1: 2, 3: 3, 16: 4, 19: 5}
say_next = 0

# spoken = {0: 1, 3: 2}
# say_next = 6
#
# spoken = {1: 1, 3: 2}
# say_next = 2
#
# spoken = {2: 1, 1: 2}
# say_next = 3
#
# spoken = {1: 1, 2: 2}
# say_next = 3

for turn in range(len(spoken) + 1, turns + 1):
    say = say_next
    if say in spoken.keys():
        say_next = turn - spoken[say]
    else:
        say_next = 0
    spoken[say] = turn


print([k for k, v in spoken.items() if v == turns][0])





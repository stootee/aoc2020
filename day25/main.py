card = 6270530
door = 14540258


def calculate(value, subject_num=7, divby=20201227):
    return (subject_num * value) % divby


def loop(door_target, card_target):
    value = loop_size = 1

    door_loop = 0
    card_loop = 0
    while not (door_loop > 0 and card_loop > 0):
        value = calculate(value)

        if value == card_target:
            card_loop = loop_size
        if value == door_target:
            door_loop = loop_size
        loop_size += 1

    return door_loop, card_loop


val = 1
for x in range(loop(door, card)[0]):
    val = (calculate(val, card))

print(val)

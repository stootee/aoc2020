def show_seating_area(sa):
    for _x in sa:
        for _c in _x:
            print(point_type(_c), end='')
        print()
    print()


def point_type(point):
    if point == '.':
        return None
    if point == 'L':
        return False
    if point == '#':
        return True
    if point == True:
        return '#'
    if point == False:
        return 'L'
    if point == None:
        return '.'


def count_adjacent(_x, _y):
    cnt = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if (_x + a == _x and _y + b == _y) or _x + a < 0 or _y + b < 0:
                _r = 0
            else:
                try:
                    _r = seating_area[_x + a][_y + b]
                    if _r is None:
                        _r = 0
                except IndexError:
                    _r = 0
            cnt += _r
    return cnt


def count_adjacent_p2(_x, _y):
    cnt = 0
    print(_x, _y, ':', end=' ')

    visibility_lines = {
        'nw': (-1, -1),
        'n': (-1, 0),
        'ne': (-1, 1),
        'e': (0, 1),
        'se': (1, 1),
        's': (1, 0),
        'sw': (1, -1),
        'w': (0, -1)
    }

    for k, v in visibility_lines.items():
        _x2, _y2 = v
        for it in range(1, max(rows, cols) + 2):
            _x2a = _x2 * it
            _y2a = _y2 * it
            # print(_x + _x2a, _y + _y2a, end=' ')
            if _x + _x2a < 0 or _y + _y2a < 0:
                # print('oob')
                break
            else:
                try:
                    _r = seating_area[_x + _x2a][_y + _y2a]
                    if _r is None:
                        # print('space')
                        continue
                    elif _r is False:
                        # print('empty seat')
                        break
                    else:
                        # print('occupied seat')
                        cnt += 1
                        break
                except IndexError:
                    # print('oob')
                    break
    return cnt


with open('input.txt') as fl:
    inp_lst = fl.read().splitlines()

# inp_lst = [
#     'L.LL.LL.LL',
#     'LLLLLLL.LL',
#     'L.L.L..L..',
#     'LLLL.LL.LL',
#     'L.LL.LL.LL',
#     'L.LLLLL.LL',
#     '..L.L.....',
#     'LLLLLLLLLL',
#     'L.LLLLLL.L',
#     'L.LLLLL.LL',
#     ]

rows, cols = len(inp_lst), len(inp_lst[0])
seating_area = []

for xn, x in enumerate(inp_lst):
    seating_row = []
    for y in x:
        seating_row.append(point_type(y))
    seating_area.append(seating_row)

changed = True
while changed:
    this_pass = []

    for rw, this_row in enumerate(seating_area):
        updated_row = []
        for cl, this_point in enumerate(this_row):

            if this_point not in (True, False):
               pass

            elif this_point and count_adjacent(rw, cl) > 3:
                this_point = False

            elif this_point is False and count_adjacent(rw, cl) == 0:
                this_point = True

            updated_row.append(this_point)
        this_pass.append(updated_row)

    # show_seating_area(seating_area)
    changed = not this_pass == seating_area
    seating_area = this_pass.copy()

count_seats = 0
for x in seating_area:
    count_seats += sum([1 for y in x if y])

print("Part 1:", count_seats)

# Part 2

seating_area = []

for xn, x in enumerate(inp_lst):
    seating_row = []
    for y in x:
        seating_row.append(point_type(y))
    seating_area.append(seating_row)

changed = True
while changed:
    this_pass = []

    for rw, this_row in enumerate(seating_area):
        updated_row = []
        for cl, this_point in enumerate(this_row):

            if this_point not in (True, False):
               pass

            elif this_point and count_adjacent_p2(rw, cl) > 4:
                this_point = False

            elif this_point is False and count_adjacent_p2(rw, cl) == 0:
                this_point = True

            updated_row.append(this_point)
        this_pass.append(updated_row)

    changed = not this_pass == seating_area
    seating_area = this_pass.copy()

show_seating_area(this_pass)
count_seats = 0
for x in seating_area:
    count_seats += sum([1 for y in x if y])

print("Part 2:", count_seats)





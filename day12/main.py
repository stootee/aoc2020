class Moves:
    def __init__(self, orientation=90, pos=(0, 0)):
        self.pos = pos
        self.orientation = orientation

    def turn(self, direction, degrees):
        multiplier = 1
        if direction == 'L':
            multiplier = -1

        self.orientation = (self.orientation + (degrees * multiplier)) % 360

    def advance(self, direction, distance):
        moves = {
            'N': (-1, 0),
            'S': (1, 0),
            'E': (0, 1),
            'W': (0, -1)
        }

        self.pos = (
            (moves[direction][0] * distance) + self.pos[0],
            (moves[direction][1] * distance) + self.pos[1]
        )

    def move(self, direction, distance):
        directions = {
            '0': 'N',
            '90': 'E',
            '180': 'S',
            '270': 'W'
        }

        if direction in ('L', 'R'):
            self.turn(direction, distance)

        elif direction == 'F':
            self.advance(directions[str(self.orientation)], distance)

        else:
            self.advance(direction, distance)


class Waypoint(Moves):
    def __init__(self, relative_pos):
        super().__init__()
        self.relative_pos = relative_pos
        self.pos = relative_pos

    def rotate(self, direction, degrees):
        degrees = degrees % 360
        for r in range(1, (degrees // 90) + 1):
            if direction == 'L':
                self.relative_pos = (self.relative_pos[1] * -1, self.relative_pos[0])
            else:
                self.relative_pos = (self.relative_pos[1], self.relative_pos[0] * -1)


class Ship(Moves):
    def __init__(self):
        super().__init__()

    def go_to_waypoint(self, coords):
        self.pos = coords
        # print('Ship:', self.pos)


with open('input.txt') as fl:
    inp_file = fl.read().splitlines()

# Part 1
ship = Ship()
for x in inp_file:
    ship.move(x[0], int(x[1:]))
print('Part 1:', ship.pos[0] + ship.pos[1])

# Part 2
ship = Ship()
waypoint = Waypoint((-1, 10))
for x in inp_file:
    if x[0] == 'F':
        for moves in range(int(x[1:])):
            coords = (ship.pos[0] + waypoint.relative_pos[0], ship.pos[1] + waypoint.relative_pos[1])
            ship.go_to_waypoint(coords)
        waypoint.pos = (ship.pos[0] + waypoint.relative_pos[0], ship.pos[1] + waypoint.relative_pos[1])
    elif x[0] in ('L', 'R'):
        waypoint.rotate(x[0], int(x[1:]))
        waypoint.pos = (ship.pos[0] + waypoint.relative_pos[0], ship.pos[1] + waypoint.relative_pos[1])
    else:
        waypoint.move(x[0], int(x[1:]))
        waypoint.relative_pos = (waypoint.pos[0] - ship.pos[0], waypoint.pos[1] - ship.pos[1])

print('Part 2:', ship.pos[0] + ship.pos[1])



course = open('day3.txt', 'r').read().splitlines()


class Toboggan:
    trees_hit = 0

    def __init__(self, pos=(0, 0), move=(3, 1)):
        self.column = pos[0]
        self.row = pos[1]
        self.across = move[0]
        self.down = move[1]

    def move(self):
        self.column += self.across
        self.row += self.down

    def i_hit_a_tree(self):
        self.trees_hit += 1


def have_i_hit_a_tree(toboggan):
    hit_tree = False
    cl = toboggan.column
    rw = toboggan.row
    if rw > len(course):
        return False

    multiplier = (cl // len(course[rw])) + 1

    if (course[rw] * multiplier)[cl] == '#':
        hit_tree = True

    return hit_tree


toboggan1 = Toboggan(move=(1, 1))
toboggan2 = Toboggan(move=(3, 1))
toboggan3 = Toboggan(move=(5, 1))
toboggan4 = Toboggan(move=(7, 1))
toboggan5 = Toboggan(move=(1, 2))

toboggans = [
    toboggan1,
    toboggan2,
    toboggan3,
    toboggan4,
    toboggan5
]

tree_multiplier = 1
for tob in toboggans:
    for moves in range(len(course)):
        if have_i_hit_a_tree(tob):
            tob.i_hit_a_tree()
        tob.move()

    print(f'{tob} hit {tob.trees_hit} trees')
    tree_multiplier *= tob.trees_hit

print(tree_multiplier)




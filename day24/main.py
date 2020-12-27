import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np


def plot(coord, color='black'):
    colors = [color] * len(coord)
    # Horizontal cartesian coords
    hcoord = [c[0] for c in coord]

    # Vertical cartesian coords
    vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]

    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')

    # Add some coloured hexagons
    for x, y, c in zip(hcoord, vcoord, colors):
        color = c[0].lower()  # matplotlib understands lower case words for colours
        hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3.,
                             orientation=np.radians(30),
                             facecolor=color, alpha=0.2, edgecolor='k')
        ax.add_patch(hex)

    # Also add scatter points in hexagon centres
    ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)

    return plt.plot()


with open('input.txt') as fl:
    inp = fl.read().splitlines()

directions = {
    'e': [1, -1, 0],
    'w': [-1, 1, 0],
    'ne': [1, 0, -1],
    'se': [0, -1, 1],
    'nw': [0, 1, -1],
    'sw': [-1, 0, 1]
}


def parse_directions(rw):
    new_rw = []
    cnt = 0
    while cnt < len(rw):
        if rw[cnt:cnt+2] in directions.keys():
            new_rw.append(rw[cnt:cnt+2])
            cnt += 2
        else:
            new_rw.append(rw[cnt])
            cnt += 1
    return new_rw


def get_distance(dirs, point=(0, 0, 0)):
    dist_from_ref_x, dist_from_ref_y, dist_from_ref_z = point
    for direction in dirs:
        dist_from_ref_x += directions[direction][0]
        dist_from_ref_y += directions[direction][1]
        dist_from_ref_z += directions[direction][2]

    return dist_from_ref_x, dist_from_ref_y, dist_from_ref_z


def part1(instructions):
    tiles = []
    for x in instructions:
        flip_tile = get_distance(parse_directions(x))
        if flip_tile in tiles:
            tiles.pop(tiles.index(flip_tile))
        else:
            tiles.append(flip_tile)

    return tiles


def adjacent(coords):
    return {
        get_distance(['ne'], coords),
        get_distance(['e'], coords),
        get_distance(['se'], coords),
        get_distance(['sw'], coords),
        get_distance(['w'], coords),
        get_distance(['nw'], coords),
    }


def part2():
    tiles = part1(inp)

    for day in range(1, 101):
        print('Day:', day)
        new_tiles = tiles.copy()
        all_adjacents = {}
        for tile in tiles:
            adjacent_tiles = adjacent(tile)
            adjacent_black = set(tiles).intersection(adjacent_tiles)
            if len(adjacent_black) == 0 or len(adjacent_black) > 2:
                new_tiles.pop(new_tiles.index(tile))
            for adj in [at for at in adjacent_tiles if at not in tiles]:
                if adj in all_adjacents.keys():
                    all_adjacents[adj] += 1
                else:
                    all_adjacents[adj] = 1
        new_tiles.extend([k for k, v in all_adjacents.items() if v == 2])
        tiles = new_tiles.copy()

    plot(tiles, 'green')
    plt.title(f'Day: {day} -- {len(tiles)} tiles')
    plt.show()
    print('Part2:', len(tiles))


pt1 = part1(inp)
plot(pt1)
plt.title('Part1')
plt.show()
print('part1:', len(pt1))

part2()

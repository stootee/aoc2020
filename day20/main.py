import numpy as np

with open('input.txt') as fl:
    input_pieces = fl.read().splitlines()


pieces = {}
piece_id = None
piece_layout = []
for ip in input_pieces:
    if ip.split(' ')[0] == 'Tile':
        piece_id = ip.split(' ')[1][:-1]
    elif len(ip) > 0:
        piece_layout.append([x for x in ip])
    else:
        pieces[piece_id] = {'layout': piece_layout}
        piece_layout = []


for piece_id, piece in pieces.items():
    edge = 0
    pl = piece['layout']
    pieces[piece_id]['edge00'] = pl[0]
    pieces[piece_id]['edge01'] = pl[0][::-1]
    for orientation in range(1, 4):
        pl = list(zip(*pl[::-1]))
        pieces[piece_id][f'edge{orientation}0'] = list(pl[0])
        pieces[piece_id][f'edge{orientation}1'] = list(pl[0][::-1])

edges = {}
for piece in pieces:
    for x in range(4):
        for y in range(2):
            edge = ''.join(pieces[piece][f'edge{x}{y}'])
            if edge in edges.keys():
                edges[edge].append({piece: f'edge{x}{y}'})
            else:
                edges[edge] = [{piece: f'edge{x}{y}'}]

pieces_without_matches = {}
for edge, matches in edges.items():

    if len(matches) == 1:
        print(edge, matches)
        ky = list(matches[0].keys())[0]
        if ky in pieces_without_matches.keys():
            pieces_without_matches[ky] += 1
        else:
            pieces_without_matches[ky] = 1


corners = [(k, v) for k, v in pieces_without_matches.items() if v > 2]
print(corners)
print('Part1:', np.product([int(k) for k, v in corners]))


def tile_variant(tile_array, orientation=0, flip=False):
    if orientation == 0 and not flip:
        return tile_array

    if orientation > 0:
        tile_array = list(zip(*tile_array[::-1]))
    if orientation > 1:
        tile_array = list(zip(*tile_array[::-1]))
    if orientation > 2:
        tile_array = list(zip(*tile_array[::-1]))
    if orientation > 3:
        tile_array = list(zip(*tile_array[::-1]))

    if flip:
        storex = []
        for x in tile_array:
            storex.append(x[::-1])
        tile_array = storex.copy()

    return tile_array

all_possible = {}
for k, v in pieces.items():
    for a in range(4):
        for b in [False, True]:
            print(k, np.array(tile_variant(v['layout'], a, b)))

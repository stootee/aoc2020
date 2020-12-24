def solve_it(puzzle, turns):

    def get_destination(num):
        found = False
        cnt = 1
        while not found:
            destination = num - cnt if num - cnt > 0 else max(puzzle)
            found = destination in puzzle
            cnt += 1

        return destination

    def pick_up(ptr, num=3):
        pu = puzzle[ptr + 1: num + 1]

        for idx in range(len(pu)):
            puzzle.pop(ptr + 1)

        return pu

    for x in range(1, turns + 1):

        this_go = puzzle[0]

        picked_up = pick_up(0)

        destination = get_destination(this_go)

        destination_idx = puzzle.index(destination)

        puzzle = puzzle[1:destination_idx + 1] + picked_up + puzzle[destination_idx + 1:]
        puzzle.append(this_go)

    return [str(x) for x in puzzle[puzzle.index(1)+1:] + puzzle[:puzzle.index(1)]]


input = '792845136'

# Part 1
print(''.join(solve_it([int(x) for x in input], 100)))


# Part 2
# build a linked list
puzzle = [int(x) for x in input]

list_size = 1000000
ll = {x+1: x+2 for x in range(list_size)}

for x in range(0, len(puzzle)-1):
    ll[puzzle[x]] = puzzle[x+1]

ll[puzzle[-1]] = 10

ll[list_size] = pointer = puzzle[0]

for turn in range(10000000):
    a = ll[pointer]
    b = ll[a]
    c = ll[b]

    pickup = [a, b, c]

    found = False
    cnt = 1
    destination = None
    while not found:
        destination = pointer - cnt if pointer - cnt > 0 else max([x for x in ll.keys() if x not in pickup])
        found = destination not in pickup
        cnt += 1

    ll[pointer] = ll[c]
    ll[c] = ll[destination]
    ll[destination] = a

    pointer = ll[pointer]

print(ll[1] * ll[ll[1]])


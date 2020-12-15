from itertools import combinations


def read_mask(inp):
    return inp[7:]


def apply_mask(bv):
    masked_binary = ''
    for m, v in zip(current_mask, bv):
        if m == 'X':
            masked_binary += v
        else:
            masked_binary += m
    return masked_binary


def apply_mask_v2(bv):
    masked_binary_values = []
    masked_binary = ''
    for m, v in zip(current_mask, bv):
        if m == '0':
            masked_binary += v
        elif m == '1':
            masked_binary += '1'
        else:
            masked_binary += 'X'

    noof_x = masked_binary.count('X')
    for xs in set(combinations([1, 0] * noof_x, noof_x)):
        new_mb = ''
        cnt_x = 0
        for char in masked_binary:
            if char == 'X':
                new_mb += str(xs[cnt_x])
                cnt_x += 1
            else:
                new_mb += char

        masked_binary_values.append(new_mb)

    return masked_binary_values


def read_mem(inp):
    return inp.split(' = ')


def write_to_mem(loc, val):
    exec(f"{loc} = {val}")


def convert_to_binary(i, length=36):
    return format(int(i), "b").zfill(length)


def convert_to_int(binary):
    return int(binary, 2)


with open('input.txt') as fl:
    input_file = fl.read().splitlines()

# Part 1
mem = {}
current_mask = 'X' * 36
for x in input_file:
    if x[:3] == 'mem':
        loc, val = read_mem(x)

        bin_val = convert_to_binary(val)

        masked_bin = apply_mask(bin_val)

        write_to_mem(loc, convert_to_int(masked_bin))

    else:
        current_mask = read_mask(x)

print('Part 1:', sum(mem.values()))

# Part 2
mem = {}
current_mask = '0' * 36
for x in input_file:
    if x[:3] == 'mem':
        loc, val = read_mem(x)
        loc = loc[4:loc.find(']')]

        bin_val = convert_to_binary(loc)

        masked_bins = apply_mask_v2(bin_val)

        for mb in masked_bins:
            write_to_mem(f'mem[{convert_to_int(mb)}]', val)

    else:
        current_mask = read_mask(x)

print('Part 2:', sum(mem.values()))

def swap_instruction(k):
    """
    swaps the command value of k if it is one of 'nop' or 'jmp'. Otherwise leaves the value as is.\n
    Returns whether the value was swapped (bool) and the new command value of k (str)
    """

    if k == 'nop':
        return True, 'jmp'
    elif k == 'jmp':
        return True, 'nop'
    else:
        return False, k


def boot_loader(inp_list):
    accumulator = None

    def has_run(idx):
        return run_log[idx] == 1

    def has_finished(idx):
        return idx == len(inp) - 1

    for inp in inp_list:
        current_index = 0
        accumulator = 0
        run_log = [0] * len(inp)
        finished = False

        while not finished:
            try:
                instr, vl = inp[current_index].split(' ')
            except IndexError:
                print('Index error')
                break
            vl = int(vl)

            if has_run(current_index):
                break

            finished = has_finished(current_index)

            run_log[current_index] += 1
            if instr == 'jmp':
                current_index += vl
            else:
                current_index += 1

            if instr == 'acc':
                accumulator += vl

        if finished:
            break

    return accumulator


def build_input(ins_dict):
    inp_list = []
    iteration = 0
    for y in range(len(ins_dict)):
        this_inp = []
        swapped = False
        for x, kv in ins_dict.items():
            k, v = kv
            if x == iteration:
                swapped, k = swap_instruction(k)

            this_inp.append(f'{k} {v}')

        if swapped:
            inp_list.append(this_inp)

        iteration += 1
    return inp_list


with open('day8.txt', 'r') as fl:
    fl_input = fl.read().splitlines()


# Day1
print("Day 1:", boot_loader([fl_input]))


# Day2
instruction_dict = dict()
for num, instruction in enumerate(fl_input):
    command, val = instruction.split(' ')
    instruction_dict[num] = (command, val)

input_list = build_input(instruction_dict)
print("Day 2:", boot_loader(input_list))




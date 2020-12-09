with open('day9.txt') as fl:
    input_list = [int(i) for i in fl.read().splitlines()]

preamble = 25


# Part 1
def check_list(lst):
    total = lst.pop()
    for x in range(0, len(lst) - 1):
        first_num = lst[x]

        for y in range(x + 1, len(lst)):
            second_num = lst[y]

            if first_num == second_num:
                continue

            if first_num + second_num == total:
                return True

    return False


check = 0
for check in range(len(input_list) - preamble):
    if not check_list(input_list[check:check + preamble + 1]):
        print("Part 1:", input_list[check + preamble])
        break


# Part 2
def find_contiguous(lst):
    target = lst.pop()

    start_idx = 0
    summed_elements = []
    running_sum = 0
    while True:
        for x in range(start_idx, len(lst)):
            running_sum += lst[x]
            summed_elements.append(lst[x])
            if running_sum == target:
                return summed_elements
            elif running_sum > target:
                start_idx += 1
                summed_elements = []
                running_sum = 0
                break


fc = find_contiguous(input_list[:check + preamble + 1])
print("Part 2:", min(fc) + max(fc))

def get_input(filename):
    with open(filename) as fl:
        return fl.read().splitlines()


def reachable(num1, num2):
    return 1 <= (num2 - num1) <= 3


def main():

    input_file = get_input('input.txt')
    input_file = [int(x) for x in input_file]
    input_file.sort()

    input_file.insert(0, 0)
    input_file.append(max(input_file) + 3)

    diff_1j = 0
    diff_3j = 0
    for idx in range(1, len(input_file) - 1):
        diff = int(input_file[idx]) - int(input_file[idx - 1])

        if diff == 1:
            diff_1j += 1
        elif diff == 3:
            diff_3j += 1
        else:
            print(f"no idea what to do with diff {diff}")
            raise

    diff_3j += 1
    print(diff_1j * diff_3j)

    # Part 2
    charger_map = {}

    for x, charger in enumerate(input_file):
        charger_map[charger] = []
        poplist = input_file[x:(x + 4)]
        while len(poplist) > 1 and reachable(poplist[0], poplist[1]):
            charger_map[charger].append(poplist[1])
            poplist.pop(1)
    # print(charger_map)

    DP = {}

    def charger_combo(ky):
        if ky == len(input_file) - 1:
            return 1
        if ky in DP:
            return DP[ky]
        ans = 0
        for x in range(ky + 1, len(input_file)):
            if input_file[x] - input_file[ky] <= 3:
                ans += charger_combo(x)
        DP[ky] = ans
        return ans

    print(charger_combo(0))
    print(DP)


if __name__ == '__main__':
    main()

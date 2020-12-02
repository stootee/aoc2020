def is2020(*args):
    return sum(args) == 2020

def iterate_list(*args):
    for lst in args:
        for idx, x in enumerate(lst):



with open('day1.txt', 'r') as fl:
    a = fl.read().splitlines()

    for idx, x in enumerate(a):
        x = int(x)
        for idy, y in enumerate(a):
            y = int(y)
            for idz, z in enumerate(a):
                z = int(z)
                if x != y != z:
                    if is2020(x, y, z):
                        print(x, y, z, x * y * z)
                        break



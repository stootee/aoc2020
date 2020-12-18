def evaluate(expr):
    expr = expr.split()
    if part2:
        expr = set_order(expr)
    val = int(expr[0])
    for x in range(1, len(expr) - 1):
        if expr[x] == '+':
            val += int(expr[x + 1])
        elif expr[x] == '*':
            val *= int(expr[x + 1])
    return str(val)


def set_order(expr):
    while expr.count('+') > 0:
        first_plus = expr.index('+')
        res = str(int(expr[first_plus - 1]) + int(expr[first_plus + 1]))
        expr[first_plus] = res
        expr.pop(first_plus - 1)
        expr.pop(first_plus)

    return expr


def unpack(expr):
    while expr.count('(') > 0:
        last_bracket = len(expr)-(expr[::-1].find('('))
        eval_this = expr[last_bracket:expr[last_bracket:].find(')')+last_bracket]
        res = evaluate(eval_this)

        expr = expr.replace(f'({eval_this})', res)

    return expr


a = '2 * 3 + (4 * 5)'
b = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
c = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
d = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'


with open('input.txt') as fl:
    expressions = fl.read().splitlines()

part2 = False
total_sum = 0
for expression in expressions:
    total_sum += int(evaluate(unpack(expression)))

print('Part1', total_sum)

part2 = True
total_sum = 0
for expression in expressions:
    total_sum += int(evaluate(unpack(expression)))

print('Part2', total_sum)

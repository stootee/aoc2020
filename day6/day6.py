with open('day6.txt', 'r') as fl:
    input_answers = fl.read().split('\n\n')

groups = []
for group in input_answers:
    grouple = ()
    for individual in group.splitlines():
        grouple += ({answer for answer in individual},)
    groups.append(grouple)

# part 1
group_counter = 0
for grouple in groups:
    group_answer_set = set()
    for y in grouple:
        group_answer_set.update(y)

    group_counter += len(group_answer_set)

print(group_counter)

# part 2
same_group_answer = 0
for grouple in groups:
    same_group_answer += len(set.intersection(*grouple))

print(same_group_answer)

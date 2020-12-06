with open('day6.txt', 'r') as fl:
    input_answers = fl.read().replace('\n\n', '|').split('|')

groups = []
for group_no, group in enumerate(input_answers):
    grouple = ()
    for individual in group.splitlines():
        grouple += ({answer for answer in individual},)
    groups.append(grouple)

# part 1
group_counter = 0
for grouple in groups:
    group_set = set()
    for y in grouple:
        group_set.update(y)

    group_counter += len(group_set)

print(group_counter)

# part 2
same_group_answer = 0
for grouple in groups:
    # print(set.intersection(*grouple))
    same_group_answer += len(set.intersection(*grouple))

print(same_group_answer)
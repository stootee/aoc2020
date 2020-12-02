passwords = open('day2.txt', 'r').read().splitlines()


class Policy:
    def __init__(self, policy):
        self.policy = policy
        policy, pwd = policy.split(':')
        policy_min_max, policy_char = policy.split()
        self.policy_min, self.policy_max = [int(i) for i in policy_min_max.split('-')]
        self.pwd = pwd.strip()
        self.policy_char = policy_char.strip()

    def rule1(self):
        return self.pwd.count(self.policy_char) in range(self.policy_min, self.policy_max + 1)

    def rule2(self):
        if self.pwd[self.policy_min-1] == self.pwd[self.policy_max-1]:
            return False

        if self.pwd[self.policy_min-1] == self.policy_char or self.pwd[self.policy_max-1] == self.policy_char:
            return True
        else:
            return False


out_of_policy = []
in_policy2 = []
for item in passwords:
    item_policy = Policy(item)

    if item_policy.rule1():
        out_of_policy.append(item)

    if item_policy.rule2():
        in_policy2.append(item)

print(len(out_of_policy))
print(len(in_policy2))






import networkx as nx


class Bag:
    children = []

    def __init__(self, name):
        self.name = name
        self.property, self.colour = name.split(' ')

    def add_child(self, name, num):
        self.children.append((name, num))


with open('day7.txt', 'r') as fl:
    inp = fl.read().splitlines()

B = nx.DiGraph()
bags = []
for rule in inp:
    parent, children = rule.split(' bags contain ')
    bag = Bag(parent)
    for child in (children.replace(' bags', '').replace(' bag', '')[:-1].split(',')):
        if not child == 'no other':
            num = int(child.strip()[:1])
            bag_name = child.strip()[2:]
            bag.add_child(bag_name, num)
            B.add_edge(parent, bag_name, weight=num)
    bags.append(bag)

node_name = 'shiny gold'

colours = {node for node in nx.bfs_edges(B, node_name, reverse=True) if node != node_name}

print(len(colours))

no_of_bags = [node for node in nx.edge_bfs(B, node_name)]

bag_map = dict()
for a, b, d in B.edges.data():
    if (a, b,) in no_of_bags:
        if a in bag_map.keys():
            bag_map[a] += [b] * d['weight']
        else:
            bag_map[a] = [b] * d['weight']

bag_list = []


def count_them_bags(bag_name):
    bag_list.append(bag_name)
    if bag_name not in bag_map.keys():
        return
    else:
        [count_them_bags(bag) for bag in bag_map[bag_name]]
        return


count_them_bags(node_name)
print(len(bag_list) - 1)

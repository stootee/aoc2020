with open('input.txt') as fl:
    inputs = fl.read().splitlines()

ingredient_list = {}
allergen_dict = {}

for row in inputs:
    ingredients, allergens = row.split('(contains ')
    allergens = [a.strip() for a in allergens[:-1].split(',')]
    ingredients = ingredients.strip().split(' ')

    for ingredient in ingredients:
        if ingredient in ingredient_list.keys():
            ingredient_list[ingredient] += 1
        else:
            ingredient_list[ingredient] = 1

    for allergen in allergens:
        if allergen in allergen_dict.keys():
            allergen_dict[allergen].append(set(ingredients))
        else:
            allergen_dict[allergen] = [set(ingredients)]

# Only keep the ingredients that appear in multiple allergen sets
for allergen, ingredients in allergen_dict.items():
    allergen_dict[allergen] = set.intersection(*ingredients)

ingredients_with_allergens = set.union(*map(set, [allergen for allergen in allergen_dict.values()]))

print('part1:', sum([vals for ingredient, vals in ingredient_list.items() if ingredient not in ingredients_with_allergens]))

cdil = {}
while len(cdil) != len(allergen_dict):
    for k, v in allergen_dict.items():
        if len(v) == 1:
            cdil[k] = list(v)[0]
        else:
            allergen_dict[k] = v.difference(set(cdil.values()))

print('part2:', ','.join([cdil[k] for k in sorted(cdil)]))


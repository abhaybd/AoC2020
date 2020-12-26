from functools import reduce

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    foods = []
    for line in lines:
        if "(contains" in line:
            ingredients_str, allergens_str = line.split("(contains")
            ingredients = ingredients_str.strip().split(" ")
            allergens = allergens_str[:-1].replace(",", "").strip().split(" ")
            foods.append((ingredients, allergens))
        else:
            foods.append((line.split(" "), []))

allergen_map = {}
for ingredients, allergens in foods:
    for allergen in allergens:
        if allergen not in allergen_map:
            allergen_map[allergen] = set(ingredients)
        else:
            allergen_map[allergen] &= set(ingredients)

while any(len(ing) != 1 for a, ing in allergen_map.items()):
    for allergen, ingredients in allergen_map.items():
        if len(ingredients) == 1:
            elem = next(iter(ingredients))
            for a, ing in allergen_map.items():
                if a != allergen and elem in ing:
                    ing.remove(elem)

allergen_ingredients = set(next(iter(ingredients)) for allergen, ingredients in allergen_map.items())
all_ingredients = reduce(lambda a, b: a+b, [ingredients for ingredients, allergens in foods])
nonallergic_ingredients = set(all_ingredients) - allergen_ingredients

# part one
print(sum(ing in nonallergic_ingredients for ing in all_ingredients))

# part two
inv_allergen_map = {next(iter(ingredients)): allergen for allergen, ingredients in allergen_map.items()}
print(",".join(sorted(list(allergen_ingredients), key=lambda x: inv_allergen_map[x])))

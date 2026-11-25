from data import INGREDIENTS


def craft(ingredients, potions, potion):
    needs = []
    for cat in potion["recipe"]:
        for name, count in ingredients.items.items():
            if INGREDIENTS[name] == cat and count > needs.count(name):
                needs.append(name)
                break
        else:
            raise ValueError(f"Немає інгредієнта категорії: {cat}")
    if potions.add(potion["name"]) == 0:
        raise OverflowError("Інвентар зілля заповнений")
    for n in needs:
        ingredients.remove(n)


def sell_all(potions, prices):
    total = 0
    for name, count in list(potions.items.items()):
        total += prices[name] * count
        potions.remove(name, count)
    return total
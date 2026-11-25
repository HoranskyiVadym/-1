import random
from data import INGREDIENTS, POTIONS, PRICES
from inventory import Inventory
from crafting import craft, sell_all

DAYS, GOAL = 30, 1200  # за 30 днів назбирати 1200 золота на Філософський камінь


def new_day(ingr):
    try:
        got = sum(ingr.add(random.choice(list(INGREDIENTS)), 1) for _ in range(5))
        print(f"Отримано інгредієнтів: {got}")
    except Exception as e:
        print("Помилка видачі:", e)


def craft_menu(ingr, pots):
    for i, p in enumerate(POTIONS, 1):
        print(f"{i}. {p['name']} = {' + '.join(p['recipe'])} ({p['price']}з)")
    try:
        craft(ingr, pots, POTIONS[int(input("Номер зілля: ")) - 1])
        print("Зілля створено!")
    except (ValueError, IndexError) as e:
        print("Не вийшло:", e)
    except OverflowError as e:
        print(e)


def main():
    ingr, pots, gold = Inventory(25, 25), Inventory(10, 10), 0
    for day in range(1, DAYS + 1):
        print(f"\n=== День {day}/{DAYS} | Золото: {gold}/{GOAL} ===")
        new_day(ingr)
        while True:
            try:
                c = input("1-Варити 2-Інвентар 3-Кінець дня: ")
                if c == "1":
                    craft_menu(ingr, pots)
                elif c == "2":
                    ingr.show("Інгредієнти")
                    pots.show("Зілля")
                elif c == "3":
                    gold += sell_all(pots, PRICES)
                    break
                else:
                    raise ValueError("Невірний вибір")
            except ValueError as e:
                print(e)
            except (KeyboardInterrupt, EOFError):
                print("\nВихід з гри.")
                return
        if gold >= GOAL:
            print(f"ПЕРЕМОГА! Ти купив Філософський камінь за {day} днів!")
            return
    print(f"ПОРАЗКА. Золота {gold}/{GOAL}, камінь купив інший алхімік.")


if name == "main":
    main()
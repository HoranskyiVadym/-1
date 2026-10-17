from tabulate import tabulate

def test_tabulate():
    data = [["Python", 1991], ["JavaScript", 1995], ["C++", 1985]]
    table = tabulate(data, headers=["Мова", "Рік створення"], tablefmt="grid")
    print(f"[Tabulate]\n{table}")
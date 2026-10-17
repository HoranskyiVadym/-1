import pandas as pd

def test_pandas():
    df = pd.DataFrame({"Предмет": ["Фізика", "Програмування"], "Оцінка": [95, 100]})
    print(f"[Pandas] Таблиця даних:\n{df}")
from mod_requests import test_requests
from mod_colorama import test_colorama
from mod_art import test_art
from mod_tabulate import test_tabulate
from mod_rich import test_rich
from mod_pydantic import test_pydantic
from mod_click import test_click
from mod_numpy import test_numpy
from mod_pandas import test_pandas
from mod_pytz import test_pytz

from mod_math import test_math
from mod_random import test_random
from mod_datetime import test_datetime
from mod_os import test_os
from mod_json import test_json

if __name__ == "__main__":
    print("=== ЗАПУСК ЛАБОРАТОРНОЇ РОБОТИ №4 ===")
    
    print("\n--- Зовнішні бібліотеки ---")
    test_requests()
    test_colorama()
    test_art()
    test_tabulate()
    test_rich()
    test_pydantic()
    test_click()
    test_numpy()
    test_pandas()
    test_pytz()
    
    print("\n--- Вбудовані бібліотеки ---")
    test_math()
    test_random()
    test_datetime()
    test_os()
    test_json()
    
    print("\n=== УСПІШНО ВИКОНАНО ВСІ 15 ФУНКЦІЙ ===")
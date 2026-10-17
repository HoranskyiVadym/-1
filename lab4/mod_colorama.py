from colorama import Fore, Style, init

def test_colorama():
    init(autoreset=True)
    print(f"[Colorama] {Fore.GREEN}Цей текст зелений і стилізований!{Style.RESET_ALL}")
import os

def test_os():
    current_dir = os.getcwd()
    print(f"[OS] Поточна робоча директорія: {current_dir}")
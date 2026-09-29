import sys

# --- ЛЯМБДА-ФУНКЦІЇ ---
format_price = lambda price: f"{price:.2f}грн"
calculate_total = lambda items: sum(map(lambda item: item['product']['price'] * item['quantity'], items))

# --- БАЗА ДАНИХ ТА СТАН ---
products = [
    {"id": 1, "name": "Ноутбук", "price": 25000.0, "stock": 5},
    {"id": 2, "name": "Мишка бездротова", "price": 450.5, "stock": 15},
    {"id": 3, "name": "Клавіатура", "price": 1200.0, "stock": 8},
    {"id": 4, "name": "Монітор 24\"", "price": 6800.99, "stock": 4},
]

cart = []
ADMIN_PASSWORD = "admin"

# --- ФУНКЦІОНАЛ МАГАЗИНУ ---
def show_catalog():
    print("\n=== КАТАЛОГ ТОВАРІВ ===")
    available = list(filter(lambda p: p['stock'] > 0, products))
    if not available:
        print("Товари відсутні.")
        return
    for p in available:
        print(f"[{p['id']}] {p['name']} - {format_price(p['price'])} (В наявності: {p['stock']} шт.)")

def add_to_cart():
    show_catalog()
    try:
        p_id = int(input("\nВведіть ID товару: "))
        product = next((p for p in products if p['id'] == p_id), None)
        if not product:
            print("Товар не знайдено.")
            return

        qty = int(input(f"Кількість для '{product['name']}': "))
        if qty <= 0:
            print("Кількість має бути більше 0.")
            return
        if qty > product['stock']:
            print(f"Недостатньо на складі! Доступно: {product['stock']}")
            return

        item = next((i for i in cart if i['product']['id'] == p_id), None)
        if item:
            if item['quantity'] + qty > product['stock']:
                print("Перевищено складський залишок!")
                return
            item['quantity'] += qty
        else:
            cart.append({'product': product, 'quantity': qty})
        print("Товар додано в кошик!")
    except ValueError:
        print("Помилка: введіть число!")

def view_cart():
    if not cart:
        print("\nКошик порожній.")
        return
    print("\n=== ВАШ КОШИК ===")
    for item in cart:
        p = item['product']
        q = item['quantity']
        print(f"[{p['id']}] {p['name']} x {q} шт. = {format_price(p['price'] * q)}")
    print(f"Загальна сума: {format_price(calculate_total(cart))}")

def remove_from_cart():
    global cart
    if not cart:
        print("\nКошик порожній.")
        return
    view_cart()
    try:
        p_id = int(input("\nВведіть ID товару для видалення: "))
        cart = list(filter(lambda item: item['product']['id'] != p_id, cart))
        print("Кошик оновлено.")
    except ValueError:
        print("Помилка: введіть число!")

def checkout():
    if not cart:
        print("\nКошик порожній!")
        return
    total = calculate_total(cart)
    for item in cart:
        item['product']['stock'] -= item['quantity']
    print(f"\nПокупку успішно здійснено на суму: {format_price(total)}")
    cart.clear()

def admin_panel():
    pwd = input("Введіть пароль адміна: ")
    if pwd != ADMIN_PASSWORD:
        print("Невірний пароль!")
        return
    print("\n=== ЗАЛИШКИ ТОВАРІВ (АДМІН) ===")
    sorted_products = sorted(products, key=lambda p: p['stock'])
    for p in sorted_products:
        print(f"ID: {p['id']} | {p['name']} | Ціна: {format_price(p['price'])} | Залишок: {p['stock']} шт.")

# --- ГОЛОВНЕ МЕНЮ ---
def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Каталог | 2. Додати в кошик | 3. Переглянути кошик")
        print("4. Видалити з кошика | 5. Купити | 6. Адмін-панель | 0. Вихід")
        choice = input("Виберіть дію: ").strip()

        if choice == "1": show_catalog()
        elif choice == "2": add_to_cart()
        elif choice == "3": view_cart()
        elif choice == "4": remove_from_cart()
        elif choice == "5": checkout()
        elif choice == "6": admin_panel()
        elif choice == "0": sys.exit()
        else: print("Невірний вибір!")

# --- ГОЛОВНА ТОЧКА ВХОДУ ---
if __name__ == "__main__":
    main()
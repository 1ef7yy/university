import os
from operator import attrgetter

class Price:
    def __init__(self, product_name="", store_name="", price=0.0):
        self.product_name = product_name
        self.store_name = store_name
        self.price = price

    def __str__(self):
        return f"{self.store_name:20} | {self.product_name:20} | {self.price:8.2f} руб."

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_window(title, content, width=60):
    border = '+' + '-' * (width - 2) + '+'
    print(border)
    print(f"| {title.center(width - 4)} |")
    print(border)
    for line in content:
        print(f"| {line.ljust(width - 4)} |")
    print(border)

def input_with_validation(prompt, validation_func=None, error_msg="", allow_exit=False):
    while True:
        try:
            if allow_exit:
                prompt += " (или 'выход' для отмены): "
            value = input(prompt)
            if allow_exit and value.lower() == 'выход':
                return None
            if validation_func and not validation_func(value):
                raise ValueError(error_msg)
            return value
        except ValueError as e:
            display_window("Ошибка", [str(e)], 60)
            input("Нажмите Enter для продолжения...")
            clear_screen()

def input_price():
    clear_screen()
    display_window("Ввод данных о товаре", ["Введите данные или 'выход' для отмены"], 60)

    product_name = input_with_validation(
        "Название товара: ",
        lambda x: len(x) > 0,
        "Название товара не может быть пустым",
        allow_exit=True
    )
    if product_name is None:
        return None

    store_name = input_with_validation(
        "Название магазина: ",
        lambda x: len(x) > 0,
        "Название магазина не может быть пустым",
        allow_exit=True
    )
    if store_name is None:
        return None

    price_str = input_with_validation(
        "Стоимость товара (руб): ",
        lambda x: x.replace('.', '', 1).isdigit() and float(x) > 0,
        "Цена должна быть положительным числом",
        allow_exit=True
    )
    if price_str is None:
        return None

    return Price(product_name, store_name, float(price_str))

def input_prices_array():
    prices = []
    for i in range(8):
        price = input_price()
        if price is None:  # Пользователь выбрал выход
            if prices:  # Если уже есть введенные товары
                confirm = input_with_validation(
                    "Сохранить уже введенные товары? (да/нет): ",
                    lambda x: x.lower() in ['да', 'нет'],
                    "Пожалуйста, введите 'да' или 'нет'"
                )
                if confirm.lower() == 'да':
                    break
                else:
                    return []
            else:
                return []
        prices.append(price)
        clear_screen()

    # Сортировка по названию магазина
    prices.sort(key=attrgetter('store_name'))
    return prices

def find_products_by_store(prices, store_name):
    found = [p for p in prices if p.store_name.lower() == store_name.lower()]
    return found if found else None

def save_to_file(prices, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for price in prices:
                f.write(f"{price.store_name};{price.product_name};{price.price}\n")
        return True
    except IOError:
        return False

def main_menu():
    prices = []

    while True:
        clear_screen()
        display_window("Главное меню", [
            "1. Ввод данных о товарах",
            "2. Поиск товаров по магазину",
            "3. Сохранить данные в файл",
            "4. Выход"
        ], 40)

        choice = input_with_validation(
            "Выберите пункт меню: ",
            lambda x: x in ['1', '2', '3', '4'],
            "Пожалуйста, введите число от 1 до 4"
        )

        if choice == '1':
            new_prices = input_prices_array()
            if new_prices:  # Если пользователь не отменил ввод
                prices = new_prices

        elif choice == '2':
            clear_screen()
            if not prices:
                display_window("Ошибка", ["Сначала введите данные о товарах!"], 60)
                input("Нажмите Enter для продолжения...")
                continue

            store_name = input_with_validation(
                "Введите название магазина: ",
                lambda x: len(x) > 0,
                "Название магазина не может быть пустым"
            )

            found = find_products_by_store(prices, store_name)
            clear_screen()

            if found:
                content = [f"Найдено товаров: {len(found)}", ""] + [str(p) for p in found]
                display_window(f"Товары в магазине '{store_name}'", content, 80)
            else:
                display_window("Результат поиска", [f"Магазин '{store_name}' не найден"], 60)

            input("Нажмите Enter для продолжения...")

        elif choice == '3':
            clear_screen()
            if not prices:
                display_window("Ошибка", ["Сначала введите данные о товарах!"], 60)
                input("Нажмите Enter для продолжения...")
                continue

            filename = input_with_validation(
                "Введите имя файла для сохранения: ",
                lambda x: len(x) > 0 and not any(c in x for c in '/\\:*?"<>|'),
                "Недопустимое имя файла"
            )

            if save_to_file(prices, filename):
                display_window("Успех", [f"Данные успешно сохранены в файл '{filename}'"], 60)
            else:
                display_window("Ошибка", ["Не удалось сохранить файл"], 60)

            input("Нажмите Enter для продолжения...")

        elif choice == '4':
            break

if __name__ == "__main__":
    main_menu()

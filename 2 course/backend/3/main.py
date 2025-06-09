# 1.1
def calculator():
    print("\nКалькулятор")
    print("Доступные операции: +, -, *, /")
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор: ")
    num2 = float(input("Введите второе число: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: деление на ноль!")
            return
    else:
        print("Неверный оператор!")
        return

    print(f"Результат: {result}")


# 1.2
def count_vowels():
    print("\nПодсчёт гласных")
    text = input("Введите текст: ").lower()
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    count = sum(1 for char in text if char in vowels)
    print(f"Количество гласных: {count}")


# 1.3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_primes():
    print("\nОпределение простых чисел")
    limit = int(input("Введите верхнюю границу: "))
    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    print(f"Простые числа до {limit}: {primes}")


# 2.1
def phone_book():
    print("\nТелефонная книга")
    contacts = {}

    while True:
        print("\n1. Добавить контакт")
        print("2. Изменить контакт")
        print("3. Удалить контакт")
        print("4. Просмотреть все контакты")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            contacts[name] = phone
            print("Контакт добавлен!")
        elif choice == '2':
            name = input("Введите имя контакта для изменения: ")
            if name in contacts:
                phone = input("Введите новый номер телефона: ")
                contacts[name] = phone
                print("Контакт обновлён!")
            else:
                print("Контакт не найден!")
        elif choice == '3':
            name = input("Введите имя контакта для удаления: ")
            if name in contacts:
                del contacts[name]
                print("Контакт удалён!")
            else:
                print("Контакт не найден!")
        elif choice == '4':
            print("\nСписок контактов:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif choice == '5':
            break
        else:
            print("Неверный выбор!")


# 2.2
def list_intersection():
    print("\nПоиск пересечения списков")
    list1 = input("Введите первый список (через пробел): ").split()
    list2 = input("Введите второй список (через пробел): ").split()
    intersection = list(set(list1) & set(list2))
    print(f"Пересечение списков: {intersection}")


# 2.3
def unique_words():
    print("\nУникальные слова в тексте")
    text = input("Введите текст: ").lower()
    words = text.split()
    unique = set(words)
    print(f"Количество уникальных слов: {len(unique)}")


# 3.1
def write_numbers():
    print("\nЗапись чисел в файл")
    filename = input("Введите имя файла: ")
    with open(filename, 'w') as file:
        for num in range(1, 101):
            file.write(f"{num}\n")
    print(f"Числа от 1 до 100 записаны в {filename}")


# 3.2
def sum_numbers():
    print("\nЧтение и сумма чисел из файла")
    filename = input("Введите имя файла: ")
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip()]
        print(f"Сумма чисел: {sum(numbers)}")
    except FileNotFoundError:
        print("Файл не найден!")
    except ValueError:
        print("Ошибка: файл содержит нечисловые данные!")


# 3.3
def student_list():
    print("\nСписок студентов")
    filename = "students.txt"

    while True:
        print("\n1. Добавить студента")
        print("2. Просмотреть список студентов")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя студента: ")
            with open(filename, 'a') as file:
                file.write(f"{name}\n")
            print("Студент добавлен!")
        elif choice == '2':
            try:
                with open(filename, 'r') as file:
                    students = [line.strip() for line in file]
                print("\nСписок студентов:")
                for student in students:
                    print(student)
            except FileNotFoundError:
                print("Список студентов пуст!")
        elif choice == '3':
            break
        else:
            print("Неверный выбор!")


# 3.4
def copy_file():
    print("\nКопирование файла")
    source = input("Введите имя исходного файла: ")
    dest = input("Введите имя целевого файла: ")

    try:
        with open(source, 'r') as src_file:
            content = src_file.read()
        with open(dest, 'w') as dst_file:
            dst_file.write(content)
        print("Файл успешно скопирован!")
    except FileNotFoundError:
        print("Исходный файл не найден!")


# 3.5
def unique_words_file():
    print("\nПодсчёт уникальных слов в файле")
    filename = input("Введите имя файла: ")
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
        words = text.split()
        unique = set(words)
        print(f"Количество уникальных слов: {len(unique)}")
    except FileNotFoundError:
        print("Файл не найден!")


def main():
    while True:
        print("\nГлавное меню")
        print("1. Часть 1: Функции")
        print("2. Часть 2: Словари и множества")
        print("3. Часть 3: Работа с файлами")
        print("4. Выход")

        part = input("Выберите часть программы: ")

        if part == '1':
            print("\nЧасть 1: Функции")
            print("1. Калькулятор")
            print("2. Подсчёт гласных")
            print("3. Определение простых чисел")
            print("4. Назад")

            choice = input("Выберите программу: ")

            if choice == '1':
                calculator()
            elif choice == '2':
                count_vowels()
            elif choice == '3':
                print_primes()
            elif choice == '4':
                continue
            else:
                print("Неверный выбор!")

        elif part == '2':
            print("\nЧасть 2: Словари и множества")
            print("1. Телефонная книга")
            print("2. Поиск пересечения списков")
            print("3. Уникальные слова в тексте")
            print("4. Назад")

            choice = input("Выберите программу: ")

            if choice == '1':
                phone_book()
            elif choice == '2':
                list_intersection()
            elif choice == '3':
                unique_words()
            elif choice == '4':
                continue
            else:
                print("Неверный выбор!")

        elif part == '3':
            print("\nЧасть 3: Работа с файлами")
            print("1. Запись чисел в файл")
            print("2. Чтение и сумма чисел из файла")
            print("3. Список студентов")
            print("4. Копирование файла")
            print("5. Подсчёт уникальных слов в файле")
            print("6. Назад")

            choice = input("Выберите программу: ")

            if choice == '1':
                write_numbers()
            elif choice == '2':
                sum_numbers()
            elif choice == '3':
                student_list()
            elif choice == '4':
                copy_file()
            elif choice == '5':
                unique_words_file()
            elif choice == '6':
                continue
            else:
                print("Неверный выбор!")

        elif part == '4':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()

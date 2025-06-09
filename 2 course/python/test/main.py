from datetime import datetime
from operator import attrgetter


class Zodiac:
    def __init__(self, last_name="", first_name="", zodiac_sign="", birthday=None):
        self.last_name = last_name
        self.first_name = first_name
        self.zodiac_sign = zodiac_sign
        self.birthday = birthday if birthday else [1, 1, 2000]

    def __str__(self):
        return (
            f"{self.last_name} {self.first_name:15} | "
            f"{self.zodiac_sign:12} | "
            f"{self.birthday[0]:02d}.{self.birthday[1]:02d}.{self.birthday[2]}"
        )

    def get_date(self):
        return datetime(self.birthday[2], self.birthday[1], self.birthday[0])


class ZodiacApp:
    def __init__(self):
        self.data = []
        self.sort_field = "date"

    def input_with_validation(self, prompt, validation_func=None, error_msg=""):
        while True:
            try:
                value = input(prompt)
                if validation_func and not validation_func(value):
                    raise ValueError(error_msg)
                return value
            except ValueError as e:
                print(f"Ошибка: {str(e)}")

    def input_person_data(self):
        print("\nВвод данных о человеке:")
        last_name = self.input_with_validation(
            "Фамилия: ", lambda x: len(x.strip()) > 0, "Фамилия не может быть пустой"
        )

        first_name = self.input_with_validation(
            "Имя: ", lambda x: len(x.strip()) > 0, "Имя не может быть пустым"
        )

        zodiac_sign = self.input_with_validation(
            "Знак зодиака: ",
            lambda x: len(x.strip()) > 0,
            "Знак зодиака не может быть пустым",
        )

        day = int(
            self.input_with_validation(
                "День рождения (1-31): ",
                lambda x: x.isdigit() and 1 <= int(x) <= 31,
                "День должен быть числом от 1 до 31",
            )
        )

        month = int(
            self.input_with_validation(
                "Месяц рождения (1-12): ",
                lambda x: x.isdigit() and 1 <= int(x) <= 12,
                "Месяц должен быть числом от 1 до 12",
            )
        )

        year = int(
            self.input_with_validation(
                "Год рождения: ",
                lambda x: x.isdigit() and 1900 <= int(x) <= datetime.now().year,
                f"Год должен быть числом от 1900 до {datetime.now().year}",
            )
        )

        return Zodiac(last_name, first_name, zodiac_sign, [day, month, year])

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.data = []
                for line in f:
                    parts = line.strip().split(";")
                    if len(parts) == 6:
                        last_name, first_name, zodiac_sign, day, month, year = parts
                        self.data.append(
                            Zodiac(
                                last_name,
                                first_name,
                                zodiac_sign,
                                [int(day), int(month), int(year)],
                            )
                        )
            self.sort_data()
            return True
        except FileNotFoundError:
            return False

    def save_to_file(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for person in self.data:
                    f.write(
                        f"{person.last_name};{person.first_name};{person.zodiac_sign};"
                        f"{person.birthday[0]};{person.birthday[1]};{person.birthday[2]}\n"
                    )
            return True
        except Exception as e:
            print(e)
            return False

    def sort_data(self):
        if self.sort_field == "date":
            self.data.sort(key=lambda x: x.get_date())
        elif self.sort_field == "name":
            self.data.sort(key=lambda x: (x.last_name, x.first_name))
        elif self.sort_field == "zodiac":
            self.data.sort(key=lambda x: x.zodiac_sign)

    def find_person(self, last_name):
        found = [p for p in self.data if p.last_name.lower() == last_name.lower()]
        return found if found else None

    def add_person(self, person):
        self.data.append(person)
        self.sort_data()

    def change_sort_field(self):
        print("\nВыбор сортировки:")
        print("1. По дате рождения")
        print("2. По фамилии и имени")
        print("3. По знаку зодиака")

        choice = self.input_with_validation(
            "Выберите поле для сортировки: ",
            lambda x: x in ["1", "2", "3"],
            "Пожалуйста, введите число от 1 до 3",
        )

        if choice == "1":
            self.sort_field = "date"
        elif choice == "2":
            self.sort_field = "name"
        elif choice == "3":
            self.sort_field = "zodiac"

        self.sort_data()
        print("Сортировка изменена")

    def show_all_data(self):
        print("\nВсе данные:")
        if not self.data:
            print("Нет данных для отображения")
        else:
            print("Фамилия       Имя          Знак зодиака   Дата рождения")
            for person in self.data:
                print(person)

    def search_person(self):
        if not self.data:
            print("\nНет данных для поиска")
            return

        last_name = self.input_with_validation(
            "\nВведите фамилию для поиска: ",
            lambda x: len(x.strip()) > 0,
            "Фамилия не может быть пустой",
        )

        found = self.find_person(last_name)

        if found:
            print(f"\nНайдено записей: {len(found)}")
            for person in found:
                print(person)
        else:
            print(f"\nЛюди с фамилией '{last_name}' не найдены")
            choice = self.input_with_validation(
                "Добавить нового человека? (да/нет): ",
                lambda x: x.lower() in ["да", "нет"],
                "Пожалуйста, введите 'да' или 'нет'",
            )

            if choice.lower() == "да":
                person = self.input_person_data()
                if person:
                    self.add_person(person)
                    print("Человек добавлен")

    def main_menu(self):
        while True:
            print("\nГлавное меню:")
            print("1. Загрузить данные из файла")
            print("2. Сохранить данные в файл")
            print("3. Добавить нового человека")
            print("4. Поиск по фамилии")
            print("5. Показать все данные")
            print("6. Изменить сортировку")
            print("7. Выход")

            choice = self.input_with_validation(
                "Выберите пункт меню: ",
                lambda x: x in ["1", "2", "3", "4", "5", "6", "7"],
                "Пожалуйста, введите число от 1 до 7",
            )

            if choice == "1":
                filename = input("Введите имя файла для загрузки: ")
                if self.load_from_file(filename):
                    print("Данные успешно загружены")
                else:
                    print("Не удалось загрузить данные")

            elif choice == "2":
                if not self.data:
                    print("Нет данных для сохранения")
                    continue

                filename = input("Введите имя файла для сохранения: ")
                if self.save_to_file(filename):
                    print("Данные успешно сохранены")
                else:
                    print("Не удалось сохранить данные")

            elif choice == "3":
                person = self.input_person_data()
                if person:
                    self.add_person(person)
                    print("Человек добавлен")

            elif choice == "4":
                self.search_person()

            elif choice == "5":
                self.show_all_data()

            elif choice == "6":
                self.change_sort_field()

            elif choice == "7":
                break


if __name__ == "__main__":
    app = ZodiacApp()
    app.main_menu()

# 1


class Calculator:
    def Add(self, x, y: float) -> float:
        return x + y

    def Sub(self, x, y: float) -> float:
        return x - y

    def Mul(self, x, y: float) -> float:
        return x * y

    def Div(self, x, y: float) -> float:
        try:
            return x / y
        except ZeroDivisionError:
            raise ValueError("На 0 делить нельзя")


calc = Calculator()

print(calc.Add(2, 1))
print(calc.Div(1, 0))


# 2


class Transport:
    def __init__(self, name: str, max_speed: float):
        self.name = name
        self.max_speed = max_speed


class Car(Transport):
    def __init__(self, fuel_type: str):
        self.fuel_type = fuel_type


class Bycicle(Transport):
    def __init__(self, type: str):
        self.type = type


class Plane(Transport):
    def __init__(self, altitude: float):
        self.altitude = altitude


# 3


class Currency:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency
        self.conversion_rates = {
            "EUR": 0.92,
            "YEN": 8,
            "RUB": 80,
        }

    def convert_to(self, target_currency: str):
        rate = self.conversion_rates.get(target_currency)
        if rate is None:
            raise Exception("no such currency")
            return
        self.amount = self.amount * rate
        self.currency = target_currency

    def show(self):
        print(f"You have {self.amount} {self.currency}s")


curr = Currency(10, "USD")
curr.show()
curr.convert_to("RUB")
curr.show()

# 4


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} RUB"


class Cart:
    def __init__(self):
        self.cart = []

    def Add(self, product: Product):
        self.cart.append(product)

    def Del(self, product: Product):
        self.cart.remove(product)

    def Show(self):
        for product in self.cart:
            print(product)


apple = Product("apple", 1)
pizza = Product("pizza", 60)
cart = Cart()
cart.Add(apple)
cart.Add(pizza)
cart.Show()
cart.Del(apple)
cart.Show()

# 5


class Animal:
    def make_sound(self):
        return "Неизвестный звук"


class Dog(Animal):
    def make_sound(self):
        return "Гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу!"


class Cow(Animal):
    def make_sound(self):
        return "Му!"


# 6
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def Area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height: float):
        self.width = width
        self.height = height

    def Area(self):
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, base, height: float):
        self.base = base
        self.height = height

    def Area(self):
        return 0.5 * self.base * self.height


# 7

class Phone:
    def __init__(self, name, phone: str):
        self.name = name
        self.phone = phone


class PhoneBook:
    def __init__(self):
        self.phoneList = []

    def Add(self, phone: Phone):
        self.phoneList.append(phone)

    def Del(self, phone: Phone):
        self.phoneList.remove(phone)

    def Find(self, name: str):
        for phone in self.phoneList:
            if phone.name == name:
                return phone.phone

    def List(self):
        print(self.phoneList)


# 8

class Account:
    def __init__(self, name: str, amount: float):
        self.name = name
        self.amount = amount

    def deposit(self, sum: float):
        self.amount += sum

    def withdraw(self, sum: float):
        if self.amount < sum:
            raise ValueError("Not enough money")

        self.amount -= sum


# 9

class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def getAverage(self):
        return sum(self.grades) / len(self.grades)


# 10

class TicTacToe:
    def __init__(self):
        self.grid = [["_"] * 3] * 3

    def Put(self, symbol: str, index: tuple(int, int)) -> bool:
        x, y = index
        if self.grid[y][x] != "_":
            return False
        self.grid[y][x] = symbol
        return True

    def CheckWin(self) -> str:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "_":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "_":
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "_":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "_":
            return self.board[0][2]

        return None

# 11
class Shape3D(ABC):
    @abstractmethod
    def Volume(self):
        pass


class Cube(Shape3D):
    def __init__(self, side: float):
        self.side = side

    def Volume(self):
        return self.side ** 3

    def SurfaceArea(self):
        return self.side ** 2 * 6


class Sphere(Shape3D):
    def __init__(self, radius: float):
        self.radius = radius

    def Volume(self):
        return 4/3 * pi * self.radius ** 3

    def SurfaceArea(self):
        return 4 * pi * self.radius ** 2

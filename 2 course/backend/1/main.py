# 1

user_name = input("Введите ваше имя: ")
print(f"Здравствуйте {user_name}!")


# 2
a, b = [float(i) for i in input("Введите числа через пробел: ").split(' ')]
print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")
print(f"a / b: {a / b}")
print(f"a // b: {a // b}")
print(f"a % b: {a % b}")

# 3
a = int(input("Введите число: "))

print("Четное" if a % 2 == 0 else "Нечетное")

# 4

age = int(input("Введите возраст: "))
print("Совершеннолетний" if age >= 18 else "Несовершеннолетний")


# 5

a, b = [float(i) for i in input("Введите длину и ширину прямоугольника через пробел: ").split(" ")]

print(f"Площадь: {a * b}")
print(f"Периметр: {2*(a+b)}")


# 6

a, b, c = [float(i) for i in input("Введите 3 числа через пробел: ").split(" ")]

print((a+b+c)/3)


# 7

strings = []

for _ in range(3):
    strings.append(input("Введите строку: "))

print(f"Длины строк: {[len(string) for string in strings]}")


# 8

a, b = [int(i) for i in input("Введите два числа через пробел: ").split(" ")]

print(f"a%b: {a % b}")
print(f"a//b: {a // b}")


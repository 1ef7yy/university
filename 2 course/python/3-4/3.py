# 19
import math
import numpy as np
# 1
R = 2


def f(x):
    if x >= -3 and x < -1:
        return x - 1
    elif -1 <= x and x <= 1:
        return 1
    elif 1 <= x and x <= 5:
        return math.sqrt(R**2-(x-3)**2)
    elif x >= 5 and x <= 7:
        return (x-5)/-2


x_begin = float(input("\nВведите xнач: "))
x_end = float(input("\nВведите xкон: "))
dx = float(input("\nВведите dx: "))

if x_begin < -3 or x_begin > 7 or x_end < -3 or x_end > 7:
    raise ValueError("out of range")

for x in np.arange(x_begin, x_end, dx):
    if x < -3 or x > 7:
        raise ValueError("out of range")
    print(f"Значение в точке {x}: {f(x)}")


# 2


def isIn(R, x, y):
    if x < -2*R or x > 2*R:
        return False
    if y < -2*R:
        return False

    if x <= 0:
        if y > 0:
            return False
        if y > (-x-2*R):
            return True
        return False
    else:
        if y < 0:
            return False
        if x**2+y**2 < R:
            return False
        if y <= 2*R and x <= 2*R:
            return True
        return False


for i in range(10):
    x, y = [float(j) for j in input(f"Введите координаты {i+1} выстрела через пробел: ").split(" ")]
    print("Попал!" if isIn(R, x, y) else "Не попал!")

# 3

acc = float(input("Введите точность: "))


def arcsin(x, xbegin) -> (int, int):
    if abs(x) >= 1:
        raise Exception("|x| должен быть < 1")

    result = x
    term = x
    n = 1
    sum_terms = 1

    while abs(term) > acc:
        term *= (2*n - 1) * (2*n - 1) * x * x / (2*n * (2*n + 1))
        result += term
        n += 1
        sum_terms += 1

        if n > 1000:
            break

    return result, sum_terms


print("\nРезультаты вычислений:")
print("+" + "-"*12 + "+" + "-"*20 + "+" + "-"*25 + "+")
print(f"| {'x':^10} | {'arcsin(x) (Тейлор)':^18} | {'Количество членов':^23} |")
print("+" + "-"*12 + "+" + "-"*20 + "+" + "-"*25 + "+")


x = x_begin
while x <= x_end + 1e-10:
    taylor_value, terms = arcsin(x, acc)
    if taylor_value is not None:
        print(f"| {x:^10.4f} | {taylor_value:^18.10f} | {terms:^23} |")

    x += dx

    print("+" + "-"*12 + "+" + "-"*20 + "+" + "-"*25 + "+")

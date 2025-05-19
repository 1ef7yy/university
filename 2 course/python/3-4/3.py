# 19
from math import sqrt
import numpy as np
# 1
R = 2


def f(x):
    if x >= -3 and x < -1:
        return x - 1
    elif -1 <= x and x <= 1:
        return 1
    elif 1 <= x and x <= 5:
        return sqrt(R**2-(x-3)**2)
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

def arcsin(x, xbegin, xend, eps)

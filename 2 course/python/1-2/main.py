# 19 вариант
# 1

from math import *


a = float(input("Введите a: "))

z1 = (((a+2)/(sqrt(2*a))) - (a/(sqrt(2*a)+2)) + (2/(a-sqrt(2*a))))*((sqrt(a) - sqrt(2)) / (a+2))

z2 = 1/(sqrt(a) + sqrt(2))


print(f"z1: {z1}")
print(f"z2: {z2}")


# 2
def f(R):
    if -3 <= R <= -1:
        return -R-1
    elif -1 < R <= 1:
        return 0
    elif 1 < R <= 5:
        return sqrt(4-(R-3)**2)
    elif 5 < R <= 7:
        return (R-5)/-2
    else:
        raise Exception("out of bounds")

R = float(input("Введите R: "))

print(f(R))

# 3

x, y = [float(i) for i in input("Введите x и y через пробел: ").split(" ")]




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

if isIn(R, x, y):
    print("Да")
else:
    print("Нет")

# x = 5 >=2
# A = {1, 3, 7, 8}
# B = {2, 4, 5, 10, 'apple'}
# C = A & B
# df = 'Антонова Антонина', 34, 'ж'
# z = 'type'
# D = [1, 'title', 2, 'content']
# print(x, '|', type(x))
# print(A, '|', type(A))
# print(B, '|', type(B))
# print(C, '|', type(C))
# print(df, '|', type(df))
# print(z, '|', type(z))
# print(D, '|', type(D))


# x = int(input())

# if x < -5:
#     print('(-inf, -5)')
# elif -5 <= x <= 5:
#     print('[-5, 5]')
# else:
#     print('(5, inf)')




# x = 10

# while x >= 0:
#     print(x)
#     x -= 3



# class Human:
#     def __init__(self, name, age, sex):
#         self.chars = {
#             'name': name,
#             'age': age,
#             'sex': sex  
#         }

# person = Human('Антон', 34, 'м')
# print(list(person.chars.keys()))



# print(list(range(2, 16)))




# print(*list(range(105, 4, -25)))




# ??????
# def reverse_even_indices(x):
#     for i in range(len(x)//2 + 1):
#         if i % 2 == 0:
#             x[i], x[-i] = x[-i], x[i]

#     return  x


# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(reverse_even_indices(x))




# import random
# import statistics as stat
# import matplotlib.pyplot as plt

# NUMBER_OF_VALUES = 100

# random_arr = [random.uniform(0,1) for _ in range(NUMBER_OF_VALUES)]

# avg = sum(random_arr) / NUMBER_OF_VALUES
# median = stat.median(random_arr)

# print(avg, median)

# plt.plot(random_arr, c='black', alpha=0.5)
# plt.show()



import math
import matplotlib.pyplot as plt

def f(x):
    return ((math.sqrt(1+math.e**math.sqrt(x) + math.cos(x**2)))/(abs(1-math.sin(x)**3))) + math.log(abs(2*x))


test_arr = list(range(2,10000))

values = list(map(f, test_arr))


plt.plot(test_arr, values, c='black', alpha=0.5)
plt.show()
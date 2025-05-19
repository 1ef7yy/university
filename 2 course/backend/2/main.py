# 1

numbers = list(range(1,11))
s = sum(numbers)
avg = s/len(numbers)
print(f"Сумма: {s}, среднее: {avg}, max: {max(numbers)}, min: {min(numbers)}")

# 2

nums = list(range(-10, 11))
pos_nums = [i for i in nums if i > 0]
squares = [i**2 for i in pos_nums]
print(f"Квадраты: {squares}")

# 3

words = ["lorem", "ipsum", "dog", "cat", "abracadabra"]
longest_word = words[0]
for i in words:
    if len(i) > len(longest_word):
        longest_word = i

print(f"longest word: {longest_word}")
uppercase_words = [i.upper() for i in words]
print(uppercase_words)

c = 0

for i in words:
    if len(i) > 5:
        c += 1
print(c)


# 4


table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

for row in table:
    print(" ".join(map(str, row)) + "\n")


# 5

import random

l = [random.randint(1, 100) for _ in range(20)]

odd = 0
even = 0

s3 = 0

for i in l:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

    if i % 3 == 0:
        s3 += 1

print(f"odd: {odd}")
print(f"even: {even}")

new_l = ["малое" if i < 50 else "большое" for i in l]

print(new_l)


# 6

class ShoppingList:
    def __init__(self):
        self.items = []

    def Add(self, item):
        self.items.append(item)

    def Remove(self, item):
        self.items.remove(item)

    def Check(self, item):
        return item in self.items

    def Print(self):
        print(sorted(self.items))


sh_list = ShoppingList()

sh_list.Add("banana")
sh_list.Add("apple")
sh_list.Add("laptop")
sh_list.Remove("apple")
sh_list.Print()
print(sh_list.Check("apple"))

# 7

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(3)] for i in range(3)]

max_in_rows = [max(row) for row in result_matrix]

print("Результирующая матрица:")
for row in result_matrix:
    print(row)

print(f"Максимальные элементы в строках: {max_in_rows}")


# 8

from collections import Counter

text = input("Введите строку текста: ")

char_frequency = Counter(text)

for char, freq in sorted(char_frequency.items()):
    print(f"'{char}': {freq}")

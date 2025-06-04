def input_array():
    n = int(input("Введите количество элементов массива: "))
    arr = []
    for i in range(n):
        element = float(input(f"Введите элемент {i+1}: "))
        arr.append(element)
    return arr


def calculate_negative_product(arr):
    product = 1
    has_negatives = False
    for num in arr:
        if num < 0:
            product *= num
            has_negatives = True
    return product if has_negatives else 0


def calculate_sum_before_max(arr):
    if not arr:
        return 0

    max_index = arr.index(max(arr))
    sum_pos = 0

    for i in range(max_index):
        if arr[i] > 0:
            sum_pos += arr[i]

    return sum_pos


def reverse_array(arr):
    return arr[::-1]


def main():
    print("Работа с одномерным массивом")
    arr = input_array()

    neg_product = calculate_negative_product(arr)
    print(f"\nПроизведение отрицательных элементов: {neg_product}")

    sum_before_max = calculate_sum_before_max(arr)
    print(f"Сумма положительных элементов до максимального: {sum_before_max}")

    reversed_arr = reverse_array(arr)
    print(f"\nМассив после изменения порядка элементов: {reversed_arr}")

main()

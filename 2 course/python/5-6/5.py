MATRIX_SIZE = 4

def input_matrix():
    matrix = []
    print(f"Введите элементы матрицы {MATRIX_SIZE}x{MATRIX_SIZE}:")
    for i in range(MATRIX_SIZE):
        row = []
        for j in range(MATRIX_SIZE):
            element = int(input(f"Элемент [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def sum_rows_without_negatives(matrix):
    sums = []
    for row in matrix:
        has_negatives = any(element < 0 for element in row)
        if not has_negatives:
            sums.append(sum(row))
    return sums

def min_sum_of_diagonals(matrix):
    n = len(matrix)
    min_sum = float('inf')

    for k in range(n):
        current_sum = 0
        i, j = 0, k
        while i < n and j < n:
            current_sum += matrix[i][j]
            i += 1
            j += 1
        if current_sum < min_sum:
            min_sum = current_sum

    for k in range(1, n):
        current_sum = 0
        i, j = k, 0
        while i < n and j < n:
            current_sum += matrix[i][j]
            i += 1
            j += 1
        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f"{elem:4}" for elem in row))

def main():
    matrix = input_matrix()

    print("\nВведенная матрица:")
    print_matrix(matrix)

    sums = sum_rows_without_negatives(matrix)
    if sums:
        print("\nСуммы элементов в строках без отрицательных элементов:")
        for i, s in enumerate(sums, 1):
            print(f"Строка {i}: {s}")
    else:
        print("\nВ матрице нет строк без отрицательных элементов")

    min_diag_sum = min_sum_of_diagonals(matrix)
    print(f"\nМинимальная сумма среди диагоналей, параллельных главной: {min_diag_sum}")


main()

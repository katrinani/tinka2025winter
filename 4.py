"""
"memoryUsed": "0.00",
"timeUsed": "0.013",
"passedTests": 7,
"score": 30
"""

def min_operations(
        n: int, x: int, y: int, z: int,
        a: list[int]
) -> int:
    """
    Определяет минимальное количество операций, нужных для деления эл-тов на x, y, z
    :param n: Количество эл-тов последовательности
    :param x: Число х
    :param y: Число y
    :param z: Число z
    :param a: Последовательность чисел
    :return: Минимальное количество операций
    """
    # Проверяем, есть ли уже элементы, кратные x, y, z
    has_x = any(ai % x == 0 for ai in a)
    has_y = any(ai % y == 0 for ai in a)
    has_z = any(ai % z == 0 for ai in a)

    if has_x and has_y and has_z:
        return 0

    # Заводим словари для пар: индекс элемента - количество операций
    operation_x = {i: (x - (a[i] % x)) if a[i] % x != 0 else 0 for i in range(n)}
    operation_y = {i: (y - (a[i] % y)) if a[i] % y != 0 else 0 for i in range(n)}
    operation_z = {i: (z - (a[i] % z)) if a[i] % z != 0 else 0 for i in range(n)}

    # Находим индексы элементов с минимальными операциями
    min_ind_x = min(operation_x, key=operation_x.get)
    min_ind_y = min(operation_y, key=operation_y.get)
    min_ind_z = min(operation_z, key=operation_z.get)

    # Все три минимальных индекса разные
    if min_ind_x != min_ind_y and min_ind_x != min_ind_z and min_ind_y != min_ind_z:
        return operation_x[min_ind_x] + operation_y[min_ind_y] + operation_z[min_ind_z]
    # Два минимальных индекса совпадают
    elif min_ind_x == min_ind_y:
        return operation_x[min_ind_x] + operation_z[min_ind_z]
    elif min_ind_x == min_ind_z:
        return operation_x[min_ind_x] + operation_y[min_ind_y]
    elif min_ind_y == min_ind_z:
        return operation_y[min_ind_y] + operation_x[min_ind_x]


if __name__ == '__main__':
    n, x, y, z = list(map(int, input().split()))
    sequence_num = list(map(int, input().split()))
    print(min_operations(n, x, y, z, sequence_num))
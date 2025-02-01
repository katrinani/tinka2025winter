"""
"memoryUsed": "0.00",
"timeUsed": "0.013",
"passedTests": 2,
"score": 5
"""

import math

def calculate_total(n: int, s: int, a: list[int]) -> int:
    """
    Вычисление суммы минимального количества частей, на которые нужно разбить каждый возможный
    подотрезок бруска, чтобы каждая часть имела длину не более s
    :param n: Количество сегментов, на которые брусок разбит засечками
    :param s: Максимальную возможная длина куска, чтобы он все еще считался маленьким
    :param a: Набор длин сегментов
    :return: Сумма по формуле
    """
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]

    total = 0
    for l in range(1, n+1):
        for r in range(l, n+1):
            segment_sum = prefix[r] - prefix[l-1]
            f_lr = math.ceil(segment_sum / s)
            total += f_lr

    return total


if __name__ == '__main__':
    count_segments, max_len = list(map(int, input().split()))
    len_segments = list(map(int, input().split()))
    print(calculate_total(count_segments, max_len,  len_segments))
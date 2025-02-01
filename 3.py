"""
"memoryUsed": "0.00",
"timeUsed": "0.013",
"passedTests": 11,
"score": 22
"""

def min_adjustments(
        n: int,
        m: int,
        days: list[int]
) -> int:
    """
    Определяет количество коректировок для того, чтобы расписание понравилось Виктории
    :param n: Количество дней до лета
    :param m: Количество хороших дней, которые нужны, чтобы расписание понравилось Виктории
    :param days: Количество километров для каждого дня
    :return: Минимальное количество корректировок

    >>> min_adjustments(3, 1, [3, 4, 6])
    2
    """
    first, second = days[0], days[1]
    adjustments = []

    for i in range(2, n):
        if days[i] < first:
            adjustments.append(first - days[i])
        elif days[i] > second:
            adjustments.append(days[i] - second)
        else:
            adjustments.append(0)

    adjustments.sort()
    return sum(adjustments[:m])



if __name__ == '__main__':
    count_days, count_goods = list(map(int, input().split()))
    all_days = list(map(int, input().split()))

    print(min_adjustments(count_days, count_goods, all_days))
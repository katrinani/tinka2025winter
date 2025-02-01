"""
"memoryUsed": "0.00",
"timeUsed": "0.012",
"passedTests": 1,
"score": 0,
"""

def prise_of_flower(count_money: int) -> int:
    """
    Подсчитывает максимально возможную стоимость трех цветков
    :param count_money: int Сумма денег, которая имеется в определенный день
    :return: Максимально близкая к сумме денег стоимость / -1

    >>> prise_of_flower(15)
    14
    >>> prise_of_flower(67)
    67
    >>> prise_of_flower(5)
    -1
    """
    # самая минимальная комбинация это 2^0 + 2^1 + 2^2 = 7
    if count_money < 7:
        return -1

    # Генерируем все степени двойки, которые меньше или равны target
    powers = [2 ** i for i in range(count_money.bit_length()) if 2 ** i <= count_money]

    # Перебираем все возможные комбинации из трёх различных степеней двойки
    closest_sum = 0

    for i in range(len(powers)):
        for j in range(i + 1, len(powers)):
            for k in range(j + 1, len(powers)):
                current_sum = powers[i] + powers[j] + powers[k]
                if count_money >= current_sum > closest_sum:
                    closest_sum = current_sum

    return closest_sum



if __name__ == '__main__':
    days = int(input())

    for _ in range(days):
        money_today = int(input())
        print(prise_of_flower(money_today))

"""
"memoryUsed": "0.00",
"timeUsed": "0.014",
"passedTests": 13,
"score": 36
"""

def compute_f(n: int, k: int, a: list[int]) -> list[int]:
    """
    Просчитывание процесса для массива чисел
    :param n: Длинна массива чисел
    :param k: Количество аргументов p, находящихся от 1 до k
    :param a: Массив чисел
    :return: Значения f(1), f(2) ... f(k)
    """
    results = []
    for p in range(1, k + 1):
        total = 0
        for i in range(n):
            for j in range(i + 1, n):
                sum_pair = a[i] + a[j]
                total = (total + pow(sum_pair, p, MOD)) % MOD
        results.append(total)
    return results


if __name__ == '__main__':
    MOD = 998244353
    count, arg = list(map(int, input().split()))
    list_num = list(map(int, input().split()))

    f_values = compute_f(count, arg, list_num)
    for value in f_values:
        print(value)
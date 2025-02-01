"""
"memoryUsed": "0.00",
"timeUsed": "0.013",
"passedTests": 33,
"score": 64
"""
from itertools import combinations

def is_collinear(p1, p2, p3):
    """Проверяет, лежат ли три точки на одной прямой."""
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

def find_max_triples(points: list[tuple[int, int]]) -> int:
    """
    Определяет максимальное количество троек жителей, таких что никакие три дома не лежат на одной прямой
    :param points: Координаты каждого дома жителя
    :return: Максимальное количество троек
    """
    # Генерируем все возможные тройки, не лежащие на одной прямой
    triples = []
    for triple in combinations(points, 3):
        if not is_collinear(*triple):
            triples.append(triple)

    # Жадный алгоритм для выбора максимального количества непересекающихся троек
    count_triples = 0
    used_points = set()

    for triple in triples:
        # Проверяем, что все точки в тройке ещё не использованы
        if all(point not in used_points for point in triple):
            used_points.update(triple)
            count_triples += 1

    return count_triples


if __name__ == '__main__':
    """
    7
    1 1
    2 2
    1 4
    6 3
    4 5
    4 1
    3 3
    """
    count_homes = int(input())
    all_coord = [tuple(list(map(int, input().split()))) for _ in range(count_homes)]
    result = find_max_triples(all_coord)
    print(result)

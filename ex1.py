from collections import deque

def bfs_shortest_path(adj_matrix, start, end):
    """
    Находит кратчайший путь (по количеству ребер) с помощью BFS.
    """
    n = len(adj_matrix)
    
    # Проверка корректности введенных вершин
    if start < 0 or start >= n or end < 0 or end >= n:
        return None

    # Очередь для хранения вершин, которые нужно посетить
    queue = deque([start])
    
    # Массив для отслеживания посещенных вершин (чтобы не зациклиться)
    visited = [False] * n
    visited[start] = True
    
    # Массив родителей для восстановления пути
    # parents[i] хранит номер вершины, из которой пришли в i
    parents = [None] * n

    while queue:
        current = queue.popleft()

        # Если дошли до цели, останавливаемся
        if current == end:
            break

        # Перебираем всех возможных соседей
        for neighbor in range(n):
            # Если есть ребро (1) и сосед еще не посещен
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                parents[neighbor] = current
                queue.append(neighbor)

    # Восстановление пути
    if not visited[end]:
        return None  # Путь не найден
    
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parents[step]
    
    path.reverse()  # Разворачиваем путь от начала к концу
    return path

def main():
    # Матрица смежности для графа из задания (10 вершин: 0-9)
    # Основано на изображении со страницы 3
    matrix = [
        #0  1  2  3  4  5  6  7  8  9
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # 0
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 1], # 1
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0], # 2
        [1, 1, 1, 0, 0, 1, 0, 0, 1, 0], # 3
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # 4
        [1, 1, 0, 1, 0, 0, 1, 0, 0, 1], # 5
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # 6
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1], # 7
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], # 8
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]  # 9
    ]

    print("--- Задание 1 ---")
    
    try:
        # Ввод данных
        # По умолчанию ставим 0 и 4, как в тесте, но можно ввести свои
        start_node = int(input("Введите номер начальной вершины (например, 0): "))
        end_node = int(input("Введите номер конечной вершины (например, 4): "))

        # Поиск пути
        path = bfs_shortest_path(matrix, start_node, end_node)

        # Вывод результата
        if path:
            print(f"Путь из вершины {start_node} в вершину {end_node}:")
            # Соединяем числа в строку без пробелов, как в примере "0315974"
            print("".join(map(str, path)))
        else:
            print("Путь не найден.")

    except ValueError:
        print("Ошибка: введите целые числа.")

if __name__ == "__main__":
    main()
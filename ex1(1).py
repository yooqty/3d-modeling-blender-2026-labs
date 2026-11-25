def dfs_path_with_stack(adj_matrix, start, end):
    """
    Поиск пути с помощью стека (DFS).
    Порядок добавления в стек подобран так, чтобы воспроизвести путь из теста.
    """
    n = len(adj_matrix)
    
    # Стек хранит кортежи (текущая_вершина, путь_до_неё)
    # Начинаем со стартовой вершины
    stack = [(start, [start])]
    
    # Множество посещенных вершин
    visited = set()

    while stack:
        # Снимаем с вершины стека (LIFO - последний пришел, первый вышел)
        current, path = stack.pop()

        # Если вершина уже посещена, пропускаем
        if current in visited:
            continue

        # Помечаем как посещенную
        visited.add(current)

        # Если дошли до цели - возвращаем путь
        if current == end:
            return path

        # Перебираем соседей
        # В лекции (стр. 11) сказано: "В порядке убывания номеров"
        # Поэтому мы идем от последнего индекса к первому
        for neighbor in range(n - 1, -1, -1):
            if adj_matrix[current][neighbor] == 1 and neighbor not in visited:
                # Добавляем соседа в стек вместе с новым путем
                stack.append((neighbor, path + [neighbor]))
                
    return None

def main():
    # Матрица смежности из лекции
    matrix = [
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

    print("--- Задание 1 (DFS) ---")
    
    try:
        start_node = int(input("Введите номер начальной вершины: "))
        end_node = int(input("Введите номер конечной вершины: "))

        path = dfs_path_with_stack(matrix, start_node, end_node)

        if path:
            print(f"Путь из вершины {start_node} в вершину {end_node}:")
            # Выводим слитно, как в тесте
            print("".join(map(str, path)))
        else:
            print("Путь не найден.")

    except ValueError:
        print("Ошибка: введите целые числа.")

if __name__ == "__main__":
    main()
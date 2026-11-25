def dfs_path(adj_matrix, start, end):
    """
    Находит путь с помощью поиска в глубину (DFS).
    Использует стек (LIFO), как описано в лекции.
    """
    n = len(adj_matrix)
    
    # Стек для хранения вершин (добавляем справа, снимаем справа)
    stack = [start]
    
    # Множество посещенных вершин
    visited = set()
    
    # Список родителей для восстановления пути
    parents = [None] * n

    while stack:
        # Снимаем вершину с вершины стека (справа)
        current = stack.pop()

        # Если вершина уже посещена, пропускаем
        if current in visited:
            continue
            
        visited.add(current)

        # Если дошли до цели — останавливаемся
        if current == end:
            break

        # Перебираем соседей
        # ВАЖНО: Чтобы получить путь как в лекции (0315974), 
        # нужно добавлять соседей в порядке возрастания номеров.
        # Так как стек снимает последний элемент, первым обработается 
        # сосед с наибольшим номером (например, 5 вместо 1).
        for neighbor in range(n):
            if adj_matrix[current][neighbor] == 1 and neighbor not in visited:
                # Если сосед еще не в стеке (или мы хотим обновить родителя)
                # Для точного совпадения с лекцией (где родитель обновляется)
                # просто добавляем в стек.
                if neighbor not in stack:
                    stack.append(neighbor)
                    parents[neighbor] = current

    # Восстановление пути
    if end not in visited:
        return None
        
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parents[step]
    
    path.reverse()
    return path

def main():
    # Матрица смежности из задания (10 вершин: 0-9)
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
        # Ввод данных
        start_node = int(input("Введите номер начальной вершины: "))
        end_node = int(input("Введите номер конечной вершины: "))

        # Поиск пути
        path = dfs_path(matrix, start_node, end_node)

        # Вывод результата
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
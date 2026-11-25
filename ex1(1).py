def get_dfs_path_like_lecture(matrix, start, end):
    n = len(matrix)
    stack = [start]
    visited = set()
    parents = [None] * n

    # Имитируем логику из лекции:
    # Мы добавляем соседей в стек, но если сосед уже в стеке,
    # мы не добавляем его заново, а "поднимаем" (перемещаем в конец).
    # Это влияет на порядок обхода.

    while stack:
        # Снимаем с вершины стека (справа)
        current = stack.pop()
        
        # Если уже посещали - пропускаем
        if current in visited:
            continue
        
        visited.add(current)

        if current == end:
            break

        # В лекции порядок добавления: перебираем соседей.
        # Чтобы получить путь 0-3-1-5-9-7-4, нам нужно,
        # чтобы при нахождении в вершине 1 (после 3), мы пошли сначала в 5, а не в 7.
        # Для этого соседи добавляются в порядке возрастания (0,1,2...),
        # но так как стек работает по принципу LIFO (последний пришел - первый ушел),
        # мы добавляем их как есть. 
        
        for neighbor in range(n):
            if matrix[current][neighbor] == 1 and neighbor not in visited:
                # Логика из лекции: если соседа нет в стеке - добавляем.
                # Если есть - перемещаем в конец (обновляем родителя).
                if neighbor in stack:
                    stack.remove(neighbor)
                
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
    # Матрица смежности (изображение 3)
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

    print("--- Задание 1 (DFS по лекции) ---")
    
    try:
        # Ввод данных с подсказками
        start_str = input("Введите номер начальной вершины (например, 0): ")
        end_str = input("Введите номер конечной вершины (например, 4): ")
        
        # Преобразование в числа
        start = int(start_str)
        end = int(end_str)

        # Получение пути
        path = get_dfs_path_like_lecture(matrix, start, end)

        if path:
            # Склеиваем цифры в строку без пробелов
            result_string = "".join(map(str, path))
            print(f"Путь из вершины {start} в вершину {end}: {result_string}")
        else:
            print("Путь не найден.")
            
    except ValueError:
        print("Ошибка: нужно вводить целые числа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
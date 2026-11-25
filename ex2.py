from collections import deque

# ==========================================
# ПОИСК В ШИРИНУ (BFS) - без изменений
# ==========================================
def bfs_path_search(adj_matrix, start_node, end_node):
    n = len(adj_matrix)
    
    visited = [False] * n
    parents = [None] * n
    distances = [None] * n
    
    queue = deque([start_node])
    visited[start_node] = True
    distances[start_node] = 0
    
    visited_list = [] 
    
    print(f"\n{'='*50}")
    print(f"--- ПОИСК В ШИРИНУ (BFS): из {start_node} в {end_node} ---")
    print(f"{'='*50}")
    
    step = 1
    while queue:
        # === ВЫВОД ТАБЛИЦЫ ПЕРЕД ШАГОМ ===
        print(f"\nШаг {step}")
        print(f"{'queue':<10} | {' '.join(map(str, queue))}")
        print(f"{'visited':<10} | {' '.join(map(str, visited_list))}")
        
        header = f"{'вершина':<10} | " + " | ".join([f"{i:2}" for i in range(n)])
        print("-" * len(header))
        print(header)
        
        dist_row = f"{'distances':<10} | " + " | ".join([f"{d if d is not None else '-':>2}" for d in distances])
        print(dist_row)
        
        parent_row = f"{'parents':<10} | " + " | ".join([f"{p if p is not None else '-':>2}" for p in parents])
        print(parent_row)
        print("-" * len(header))
        # ===================================

        current = queue.popleft()
        
        if current == end_node:
            visited_list.append(current)
            print(f"\nЦель {end_node} найдена на шаге {step}!")
            break
            
        for neighbor in range(n):
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                parents[neighbor] = current
                distances[neighbor] = distances[current] + 1
        
        visited_list.append(current)
        step += 1

    # Восстановление пути
    if not visited[end_node]:
        print(f"Путь из {start_node} в {end_node} не существует.")
        return

    path = []
    curr = end_node
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    
    path.reverse()
    
    print("\n" + "="*40)
    print(f"Кратчайший путь (по ребрам): {' -> '.join(map(str, path))}")
    print(f"Длина пути: {distances[end_node]} ребер.")
    print("="*40)


# ==========================================
# ПОИСК В ГЛУБИНУ (DFS) - Стек
# ==========================================
def dfs_path_search(adj_matrix, start_node, end_node):
    n = len(adj_matrix)
    
    visited = [False] * n
    parents = [None] * n
    # В DFS расстояния не важны, но для порядка сохраним
    distances = [None] * n 
    
    # Стек (LIFO). В методичке: добавляем справа, снимаем справа.
    stack = [start_node]
    
    visited_list = []
    
    print(f"\n{'='*50}")
    print(f"--- ПОИСК В ГЛУБИНУ (DFS): из {start_node} в {end_node} ---")
    print(f"{'='*50}")
    
    step = 1
    while stack:
        # === ВЫВОД ТАБЛИЦЫ ПЕРЕД ШАГОМ ===
        print(f"\nШаг {step}")
        print(f"{'stack':<10} | {' '.join(map(str, stack))}")
        print(f"{'visited':<10} | {' '.join(map(str, visited_list))}")
        
        header = f"{'вершина':<10} | " + " | ".join([f"{i:2}" for i in range(n)])
        print("-" * len(header))
        print(header)
        
        dist_row = f"{'distances':<10} | " + " | ".join([f"{d if d is not None else '-':>2}" for d in distances])
        print(dist_row)
        
        parent_row = f"{'parents':<10} | " + " | ".join([f"{p if p is not None else '-':>2}" for p in parents])
        print(parent_row)
        print("-" * len(header))
        # ===================================

        # Снимаем из стека СПРАВА
        current = stack.pop()
        
        # Если уже посещали (в стеке могли быть дубликаты), пропускаем
        if visited[current]:
            continue
            
        visited[current] = True
        visited_list.append(current)
        
        # Если дошли до цели
        if current == end_node:
            print(f"\nЦель {end_node} найдена на шаге {step}!")
            break
            
        # Перебираем соседей
        # В методичке сказано: "В порядке убывания номеров" (чтобы меньшие оказались на вершине стека)
        # Но для простоты пойдем по возрастанию, добавляя в стек.
        # Чтобы имитировать поведение из PDF (где соседи идут по порядку), 
        # пройдемся по соседям в обратном порядке, чтобы первый сосед оказался на вершине стека.
        for neighbor in range(n - 1, -1, -1):
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                # Если соседа нет в стеке, добавляем
                if neighbor not in stack:
                    stack.append(neighbor)
                    parents[neighbor] = current
                    distances[neighbor] = distances[current] + 1 if distances[current] is not None else 1
                else:
                    # Если сосед уже в стеке, методичка говорит "передвигаем на вершину стека"
                    # и "запоминаем нового родителя".
                    stack.remove(neighbor)
                    stack.append(neighbor)
                    parents[neighbor] = current
        
        step += 1

    # Восстановление пути
    if not visited[end_node]:
        print(f"Путь из {start_node} в {end_node} не существует.")
        return

    path = []
    curr = end_node
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    
    path.reverse()
    
    print("\n" + "="*40)
    print(f"Путь (DFS, не обязательно кратчайший): {' -> '.join(map(str, path))}")
    print(f"Длина пути: {len(path) - 1} ребер.")
    print("="*40)


# ==========================================
# 1. Ввод данных (матрица из задания)
# ==========================================
adjacency_matrix = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # 0
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0], # 1
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0], # 2
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], # 3
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # 4
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1], # 5
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0], # 6
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0], # 7
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1], # 8
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]  # 9
]

# Тест: из 0 в 4
start_vertex = 0
end_vertex = 4

# Запуск обоих алгоритмов
bfs_path_search(adjacency_matrix, start_vertex, end_vertex)
dfs_path_search(adjacency_matrix, start_vertex, end_vertex)
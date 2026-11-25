from collections import deque

def bfs_path_search(adj_matrix, start_node, end_node):
    n = len(adj_matrix)
    
    # Инициализация структур данных
    visited = [False] * n
    parents = [None] * n
    distances = [None] * n
    
    # Очередь для BFS
    queue = deque([start_node])
    
    # Настройка стартовой вершины
    visited[start_node] = True
    distances[start_node] = 0
    
    # Для красивого вывода таблиц
    visited_list = [] 
    
    print(f"--- Начало поиска BFS: из {start_node} в {end_node} ---")
    
    step = 1
    while queue:
        # === ВЫВОД ТАБЛИЦЫ ПЕРЕД ШАГОМ ===
        print(f"\nШаг {step}")
        print(f"{'queue':<10} | {' '.join(map(str, queue))}")
        print(f"{'visited':<10} | {' '.join(map(str, visited_list))}")
        
        # Формируем строки для таблицы расстояний и родителей
        header = f"{'вершина':<10} | " + " | ".join([f"{i:2}" for i in range(n)])
        print("-" * len(header))
        print(header)
        
        dist_row = f"{'distances':<10} | " + " | ".join([f"{d if d is not None else '-':>2}" for d in distances])
        print(dist_row)
        
        parent_row = f"{'parents':<10} | " + " | ".join([f"{p if p is not None else '-':>2}" for p in parents])
        print(parent_row)
        print("-" * len(header))
        # ===================================

        # Снимаем из очереди СЛЕВА (FIFO)
        current = queue.popleft()
        
        # Если дошли до цели, можем остановиться
        if current == end_node:
            visited_list.append(current)
            print(f"\nЦель {end_node} найдена на шаге {step}!")
            break
            
        # Перебираем соседей
        for neighbor in range(n):
            # Если есть ребро (1) и сосед не посещен
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                parents[neighbor] = current
                distances[neighbor] = distances[current] + 1
        
        # Добавляем текущую вершину в список посещенных (для вывода)
        visited_list.append(current)
        step += 1

    # --- Восстановление пути ---
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
# 1. Ввод данных (согласно вашему примеру)
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

# Тест из задания 1: из 0 в 4
start_vertex = 0
end_vertex = 4

# Запуск
bfs_path_search(adjacency_matrix, start_vertex, end_vertex)
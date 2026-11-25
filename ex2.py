from collections import deque

def bfs_path_search(adj_matrix, start_node, end_node):
    n = len(adj_matrix)
    
    # Инициализация структур данных (как на стр. 4 методички)
    visited = [False] * n
    parents = [None] * n
    distances = [None] * n
    
    # Очередь для BFS
    queue = deque([start_node])
    
    # Настройка стартовой вершины
    visited[start_node] = True
    distances[start_node] = 0
    
    # История посещений для вывода таблицы (доп. баллы)
    visit_order = []
    
    print(f"--- Начало поиска BFS: из {start_node} в {end_node} ---")
    
    step = 1
    while queue:
        # Снимаем из очереди СЛЕВА (FIFO)
        current = queue.popleft()
        visit_order.append(current)
        
        # Если дошли до цели, можем остановиться (или продолжить, чтобы заполнить таблицу полностью)
        if current == end_node:
            print(f"Цель {end_node} найдена на шаге {step}!")
            break
            
        # Перебираем соседей
        for neighbor in range(n):
            # Если есть ребро (1) и сосед не посещен
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                # Добавляем в очередь СПРАВА
                queue.append(neighbor)
                # Помечаем как посещенного
                visited[neighbor] = True
                # Запоминаем родителя
                parents[neighbor] = current
                # Обновляем расстояние
                distances[neighbor] = distances[current] + 1
        
        step += 1

    # --- Восстановление пути ---
    if not visited[end_node]:
        print(f"Путь из {start_node} в {end_node} не существует.")
        return

    # Идем от конца к началу по родителям
    path = []
    curr = end_node
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    
    # Переворачиваем путь (от начала к концу)
    path.reverse()
    
    # --- Вывод результатов (как на стр. 6-9) ---
    print("\n" + "="*40)
    print("ТАБЛИЦА ПОСЕЩЕННЫХ ВЕРШИН (Queue & Visited)")
    print(f"Порядок извлечения из очереди: {visit_order}")
    
    print("\nТАБЛИЦА РАССТОЯНИЙ И РОДИТЕЛЕЙ:")
    header = "Вершина | " + " | ".join([str(i) for i in range(n)])
    print("-" * len(header))
    print(header)
    
    dist_str = "Дистан | " + " | ".join([str(d) if d is not None else "-" for d in distances])
    print(dist_str)
    
    parent_str = "Родитель| " + " | ".join([str(p) if p is not None else "-" for p in parents])
    print(parent_str)
    print("="*40)

    print(f"\nКратчайший путь (по ребрам): {' -> '.join(map(str, path))}")
    print(f"Длина пути: {distances[end_node]} ребер.")

# ==========================================
# 1. Ввод данных (согласно вашему примеру)
# ==========================================

# Матрица смежности из задания (10x10)
# 0 - нет ребра, 1 - есть ребро
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
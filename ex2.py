import sys
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Базовая матрица смежности из задания
BASE_MATRIX = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # 0
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0], # 1
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0], # 2
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 0], # 3
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # 4
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 1], # 5
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0], # 6
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1], # 7
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], # 8
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0]  # 9
]

def print_matrix(matrix):
    """Красивый вывод матрицы смежности"""
    print("    " + " ".join([f"{i:2}" for i in range(len(matrix))]))
    print("   " + "---" * len(matrix))
    for i, row in enumerate(matrix):
        print(f"{i:2} | " + " ".join([f"{val:2}" for val in row]))

def edit_matrix(matrix):
    """Функция для изменения матрицы смежности по усмотрению"""
    print("\nТекущая матрица смежности:")
    print_matrix(matrix)
    
    print("\nХотите изменить матрицу? (y/n): ")
    choice = input().strip().lower()
    if choice == 'y':
        print("Введите новую матрицу построчно (числа через пробел).")
        print(f"Формат: {len(matrix)} строк по {len(matrix)} чисел.")
        new_matrix = []
        for i in range(len(matrix)):
            while True:
                try:
                    row = list(map(int, input(f"Строка {i}: ").strip().split()))
                    if len(row) == len(matrix):
                        new_matrix.append(row)
                        break
                    else:
                        print(f"Ошибка: нужно ввести ровно {len(matrix)} чисел.")
                except ValueError:
                    print("Ошибка: вводите только целые числа.")
        print("\nНовая матрица принята.")
        print_matrix(new_matrix)
        return new_matrix
    return matrix

def bfs_with_steps(matrix, start, end):
    """BFS с записью шагов для таблицы (Дополнительные баллы)"""
    n = len(matrix)
    # Очередь хранит кортежи: (текущая_вершина, путь_до_неё)
    queue = deque([(start, [start])])
    visited = {start}
    
    steps_log = [] # Для таблицы
    
    while queue:
        # Фиксируем состояние ДО извлечения
        queue_str = ", ".join([str(node) for node, _ in queue])
        visited_str = ", ".join(sorted(map(str, visited)))
        
        current, path = queue.popleft()
        
        # Записываем шаг
        steps_log.append({
            "step": len(steps_log) + 1,
            "queue": queue_str,
            "visited": visited_str,
            "current": current
        })
        
        if current == end:
            return path, steps_log
        
        # Добавляем соседей
        for neighbor in range(n):
            if matrix[current][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None, steps_log

def dfs_with_steps(matrix, start, end):
    """DFS (итеративный) с записью шагов для таблицы"""
    n = len(matrix)
    # Стек хранит кортежи: (текущая_вершина, путь_до_неё)
    stack = [(start, [start])]
    visited = set()
    steps_log = []
    
    while stack:
        # Фиксируем состояние ДО извлечения
        stack_str = ", ".join([str(node) for node, _ in stack])
        visited_str = ", ".join(sorted(map(str, visited)))
        
        current, path = stack.pop()
        
        if current in visited:
            continue
            
        visited.add(current)
        
        # Записываем шаг
        steps_log.append({
            "step": len(steps_log) + 1,
            "stack": stack_str,
            "visited": visited_str,
            "current": current
        })
        
        if current == end:
            return path, steps_log
        
        # Получаем соседей и добавляем в стек в ОБРАТНОМ порядке,
        # чтобы первым извлекался сосед с наименьшим номером (как в методичке)
        neighbors = [i for i in range(n) if matrix[current][i] == 1]
        for neighbor in sorted(neighbors, reverse=True):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
                
    return None, steps_log

def draw_graph(matrix, path, title):
    """Отрисовка графа с выделением найденного пути."""
    G = nx.Graph()
    n = len(matrix)
    G.add_nodes_from(range(n))
    
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    
    nx.draw_networkx_nodes(G, pos, node_color='lightgray', node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
        
    plt.title(title)
    plt.axis('off')
    plt.show()

def get_valid_input(prompt, max_val):
    while True:
        try:
            val = int(input(prompt).strip())
            if 0 <= val < max_val:
                return val
            else:
                print(f"Ошибка: вершина должна быть от 0 до {max_val - 1}.")
        except ValueError:
            print("Ошибка: введите целое число.")

def main():
    n = len(BASE_MATRIX)
    matrix = BASE_MATRIX.copy()
    
    # 1. Изменение матрицы по усмотрению преподавателя
    matrix = edit_matrix(matrix)
    
    # 2. Ввод вершин
    print("\n--- ВВОД ВЕРШИН ---")
    start_node = get_valid_input("Введите номер начальной вершины: ", n)
    end_node = get_valid_input("Введите номер конечной вершины: ", n)

    print("\n--- РЕЗУЛЬТАТЫ ---")

    # --- BFS ---
    print("\n[Поиск в ширину (BFS)]")
    path_bfs, log_bfs = bfs_with_steps(matrix, start_node, end_node)
    
    if path_bfs:
        bfs_str = "".join(map(str, path_bfs))
        print(f"Найденный путь: {bfs_str}")
        
        # Вывод таблицы для BFS
        print("\nТаблица посещенных вершин (BFS):")
        print(f"{'Шаг':<4} | {'Очередь':<20} | {'Посещенные':<20} | {'Текущая':<8}")
        print("-" * 60)
        for log in log_bfs:
            print(f"{log['step']:<4} | {log['queue']:<20} | {log['visited']:<20} | {log['current']:<8}")
    else:
        print("Путь не найден.")

    # --- DFS ---
    print("\n[Поиск в глубину (DFS)]")
    path_dfs, log_dfs = dfs_with_steps(matrix, start_node, end_node)
    
    if path_dfs:
        dfs_str = "".join(map(str, path_dfs))
        print(f"Найденный путь: {dfs_str}")
        
        # Вывод таблицы для DFS
        print("\nТаблица посещенных вершин (DFS):")
        print(f"{'Шаг':<4} | {'Стек':<20} | {'Посещенные':<20} | {'Текущая':<8}")
        print("-" * 60)
        for log in log_dfs:
            print(f"{log['step']:<4} | {log['stack']:<20} | {log['visited']:<20} | {log['current']:<8}")
    else:
        print("Путь не найден.")

    # Отрисовка графиков
    if path_bfs:
        draw_graph(matrix, path_bfs, f"BFS (Задание 2): путь {bfs_str}")
    if path_dfs:
        draw_graph(matrix, path_dfs, f"DFS (Задание 2): путь {dfs_str}")

if __name__ == "__main__":
    main()
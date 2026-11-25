import sys
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Матрица смежности для графа из лекции (10 вершин: 0-9)
MATRIX = [
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

def bfs_path(matrix, start, end):
    """Поиск в ширину (BFS). Находит кратчайший путь по количеству ребер."""
    n = len(matrix)
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path
        
        for neighbor in range(n):
            if matrix[current][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None

def dfs_path(matrix, start, end):
    """
    Поиск в глубину (DFS).
    Чтобы получить путь 0315974, мы добавляем соседей в порядке убывания,
    тогда первым из стека выйдет сосед с наименьшим номером.
    """
    n = len(matrix)
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        current, path = stack.pop()
        
        if current in visited:
            continue
            
        visited.add(current)
        
        if current == end:
            return path
        
        neighbors = [i for i in range(n) if matrix[current][i] == 1]
        
        # Добавляем в стек в обратном порядке (чтобы наименьший номер был на вершине)
        for neighbor in sorted(neighbors, reverse=True):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
                
    return None

def draw_graph(matrix, path, title):
    """Отрисовка графа с выделением найденного пути."""
    G = nx.Graph()
    n = len(matrix)
    
    G.add_nodes_from(range(n))
    
    # Добавляем ребра
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    
    # Жестко заданные координаты (чтобы граф выглядел как на картинке в PDF)
    pos = {
        0: (10, 5),    # Красная вершина (цель)
        1: (3, 6),     # Центральная левая
        2: (4, 9),     # Верхняя левая
        3: (7, 8.5),   # Верхняя правая
        4: (-2, 2),    # Самая левая нижняя
        5: (5, 4),     # Центральная нижняя
        6: (4.5, 1.5), # Нижняя
        7: (0.5, 3.5), # Левее центра
        8: (7, 10),    # Самая верхняя
        9: (2, 2)      # Нижняя левая
    }

    plt.figure(figsize=(10, 7))
    
    # Рисуем весь граф
    nx.draw_networkx_nodes(G, pos, node_color='lightgray', node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    # Выделяем путь красным цветом
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=600)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
        
    plt.title(title, fontsize=14)
    plt.axis('off')
    plt.show()

def get_valid_input(prompt, max_val):
    """Вспомогательная функция для корректного ввода вершин."""
    while True:
        try:
            val = int(input(prompt).strip())
            if 0 <= val < max_val:
                return val
            else:
                print(f"Ошибка: вершина должна быть в диапазоне от 0 до {max_val - 1}.")
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

def main():
    n = len(MATRIX)
    print("="*40)
    print("ЗАДАНИЕ 1: ПОИСК ПУТИ В ГРАФЕ")
    print("="*40)
    
    # Ввод данных
    start_node = get_valid_input("Введите номер начальной вершины (0-9): ", n)
    end_node = get_valid_input("Введите номер конечной вершины (0-9): ", n)

    print("\n--- РЕЗУЛЬТАТЫ ---")

    # BFS
    path_bfs = bfs_path(MATRIX, start_node, end_node)
    if path_bfs:
        bfs_str = "".join(map(str, path_bfs))
        print(f"Путь BFS (кратчайший): {bfs_str}")
    else:
        print("BFS: Путь не найден.")

    # DFS
    path_dfs = dfs_path(MATRIX, start_node, end_node)
    if path_dfs:
        dfs_str = "".join(map(str, path_dfs))
        print(f"Путь DFS (глубокий):   {dfs_str}")
    else:
        print("DFS: Путь не найден.")

    # Отрисовка графиков
    if path_bfs:
        draw_graph(MATRIX, path_bfs, f"Поиск в ширину (BFS): путь {bfs_str}")
    if path_dfs and path_bfs != path_dfs:
        # Показываем второй график, только если пути отличаются
        draw_graph(MATRIX, path_dfs, f"Поиск в глубину (DFS): путь {dfs_str}")

if __name__ == "__main__":
    main()
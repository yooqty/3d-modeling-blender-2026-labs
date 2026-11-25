from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs_shortest_path(adj_matrix, start, end):
    """
    Находит кратчайший путь (по количеству ребер) с помощью BFS.
    """
    n = len(adj_matrix)
    
    if start < 0 or start >= n or end < 0 or end >= n:
        return None

    queue = deque([start])
    visited = [False] * n
    visited[start] = True
    parents = [None] * n

    while queue:
        current = queue.popleft()
        if current == end:
            break

        for neighbor in range(n):
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                parents[neighbor] = current
                queue.append(neighbor)

    if not visited[end]:
        return None
    
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parents[step]
    
    path.reverse()
    return path

def draw_graph(adj_matrix, path):
    """
    Рисует граф и выделяет найденный путь.
    """
    # Создаем граф из матрицы смежности
    G = nx.from_numpy_array(adj_matrix) if hasattr(adj_matrix, 'shape') else nx.Graph()
    
    # Если матрица задана списком списков, строим граф вручную
    if not hasattr(adj_matrix, 'shape'):
        G = nx.Graph()
        n = len(adj_matrix)
        G.add_nodes_from(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if adj_matrix[i][j] == 1:
                    G.add_edge(i, j)

    # Задаем координаты вершин (чтобы граф выглядел как на картинке из лекции)
    # Эти координаты подобраны примерно под структуру графа из PDF
    pos = {
        0: (10, 5),    # Красная вершина справа
        1: (3, 6),     # Центральная левая
        2: (4, 9),     # Верхняя левая
        3: (7, 8.5),   # Верхняя правая (с плюсом)
        4: (-2, 2),    # Самая левая нижняя
        5: (5, 4),     # Центральная нижняя
        6: (4.5, 1.5), # Нижняя
        7: (0.5, 3.5), # Левее центра
        8: (7, 10),    # Самая верхняя
        9: (2, 2)      # Нижняя левая
    }

    plt.figure(figsize=(10, 7))
    
    # Рисуем все вершины и ребра (по умолчанию)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Выделяем найденный путь
    if path:
        # Создаем список ребер для пути
        path_edges = list(zip(path, path[1:]))
        
        # Рисуем ребра пути красным цветом и потолще
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
        
        # Выделяем вершины пути
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='salmon', node_size=600)
        
        # Подписываем вершины пути их порядковым номером в маршруте (опционально)
        # nx.draw_networkx_labels(G, pos, labels={node: f"{node}" for node in path}, font_color='black')

    plt.title("Визуализация графа и найденного пути (BFS)")
    plt.axis('off') # Отключаем оси координат
    plt.show()

def main():
    # Матрица смежности для графа из задания (10 вершин: 0-9)
    matrix = [
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]
    ]

    print("--- Задание 1 ---")
    
    try:
        start_node = int(input("Введите номер начальной вершины (например, 0): "))
        end_node = int(input("Введите номер конечной вершины (например, 4): "))

        path = bfs_shortest_path(matrix, start_node, end_node)

        if path:
            print(f"Путь из вершины {start_node} в вершину {end_node}:")
            print("".join(map(str, path)))
            
            # Вызов функции отрисовки
            draw_graph(matrix, path)
        else:
            print("Путь не найден.")

    except ValueError:
        print("Ошибка: введите целые числа.")

if __name__ == "__main__":
    main()
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# ==========================================
# 1. ВВОД ГРАФА
# ==========================================
nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

# Веса ребер:
# S-A: 1, S-B: 2, S-C: 3
# A-D: 4, B-E: 5
# C-F: 7 (исправлено по вашему замечанию)
# D-G: 7
# F-G: 1, E-G: 1 (без цифр = 1)

edges = [
    ('S', 'A', 1), ('S', 'B', 2), ('S', 'C', 3),
    ('A', 'D', 4), ('B', 'E', 5),
    ('C', 'F', 7), ('F', 'G', 1),
    ('E', 'G', 1), ('D', 'G', 7)
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# ==========================================
# 2. АЛГОРИТМ BFS (Поиск в ширину с учетом весов)
# ==========================================
def bfs_shortest_paths(graph, start_node):
    # Очередь хранит кортежи (вершина, путь_до_нее, суммарное_расстояние)
    queue = deque([(start_node, [start_node], 0)])
    
    # Словарь для хранения лучших результатов: {вершина: (путь, расстояние)}
    results = {start_node: ([start_node], 0)}

    while queue:
        current_node, path, dist = queue.popleft()

        for neighbor in graph.neighbors(current_node):
            edge_weight = graph[current_node][neighbor]['weight']
            new_dist = dist + edge_weight
            
            # Если вершина еще не посещена ИЛИ найден более короткий путь
            if neighbor not in results or new_dist < results[neighbor][1]:
                new_path = path + [neighbor]
                results[neighbor] = (new_path, new_dist)
                queue.append((neighbor, new_path, new_dist))
                
    return results

# ==========================================
# 3. ВЫВОД ТАБЛИЦЫ РЕЗУЛЬТАТОВ
# ==========================================
def print_bfs_table(results):
    print("\n" + "="*60)
    print(f"{'Метод поиска в ширину (BFS) от вершины S':^60}")
    print("="*60)
    print(f"| {'Вершина':^8} | {'Путь (маршрут)':^26} | {'Расстояние':^10} |")
    print("-" * 60)
    
    # Выводим вершины в нужном порядке
    order = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    for node in order:
        if node in results:
            path, dist = results[node]
            path_str = " -> ".join(path)
            if node == 'S':
                path_str = "S (старт)"
            print(f"| {node:^8} | {path_str:^26} | {dist:^10} |")
    print("="*60 + "\n")

# ==========================================
# 4. ВЫВОД РИСУНКА ГРАФА
# ==========================================
def draw_graph():
    plt.figure(figsize=(8, 6))
    
    pos = {
        'S': (0.5, 1.0),
        'A': (0.2, 0.7), 'B': (0.5, 0.7), 'C': (0.8, 0.7),
        'D': (0.2, 0.3), 'E': (0.5, 0.3), 'F': (0.8, 0.3),
        'G': (0.5, 0.0)
    }
    
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightgray', 
            font_size=12, font_weight='bold', edge_color='gray', width=2)
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
    
    plt.title("Задание 1. Граф (Рис.1)")
    plt.axis('off')
    plt.show()

# ==========================================
# ЗАПУСК
# ==========================================
if __name__ == "__main__":
    # 1. Сначала считаем пути
    bfs_results = bfs_shortest_paths(G, 'S')
    
    # 2. Выводим таблицу в консоль
    print_bfs_table(bfs_results)
    
    # 3. Затем показываем картинку
    draw_graph()
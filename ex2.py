import networkx as nx
import matplotlib.pyplot as plt

# ==========================================
# 1. ВВОД ГРАФА (Матрица расстояний по Рис.2)
# ==========================================
nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

# Веса ребер согласно Рис.2
edges = [
    ('S', 'A', 1), ('S', 'C', 1), ('S', 'B', 1),
    ('C', 'F', 7),
    ('F', 'G', 6),
    ('G', 'D', 3),
    ('D', 'A', 2),
    ('G', 'E', 4),
    ('E', 'B', 5)
]

# Создаем неориентированный граф
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# ==========================================
# 2. ВЫВОД РИСУНКА ГРАФА
# ==========================================
def draw_graph():
    plt.figure(figsize=(8, 6))
    
    # Координаты для отрисовки (как на картинке)
    pos = {
        'S': (0.5, 1.0),
        'A': (0.2, 0.7), 'B': (0.5, 0.7), 'C': (0.8, 0.7),
        'D': (0.2, 0.3), 'E': (0.5, 0.3), 'F': (0.8, 0.3),
        'G': (0.5, 0.0)
    }
    
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightgreen', 
            font_size=12, font_weight='bold', edge_color='black', width=2)
    
    # Подписываем веса
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
    
    plt.title("Задание 2. Граф (Рис.2) для обхода в глубину (DFS)")
    plt.axis('off')
    plt.show()

# ==========================================
# 3. АЛГОРИТМ DFS (Поиск в глубину)
# ==========================================
def dfs_paths(graph, start_node):
    # Стек хранит: (текущая_вершина, путь, суммарное_расстояние)
    stack = [(start_node, [start_node], 0)]
    visited = set()
    results = {}
    
    while stack:
        current_node, path, dist = stack.pop()
        
        if current_node not in visited:
            visited.add(current_node)
            results[current_node] = (path, dist)
            
            # Для DFS важно, в каком порядке мы добавляем соседей в стек.
            # Чтобы обход шел от S -> A -> D -> G (как на Рис.2), 
            # мы должны добавлять соседей в обратном порядке.
            neighbors = list(graph.neighbors(current_node))
            # Сортируем по алфавиту в обратном порядке (C, B, A), 
            # чтобы первой из стека досталась A.
            neighbors.sort(reverse=True)
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    weight = graph[current_node][neighbor]['weight']
                    stack.append((neighbor, path + [neighbor], dist + weight))
                    
    return results

# ==========================================
# 4. ВЫВОД ТАБЛИЦЫ
# ==========================================
def print_dfs_table(results):
    print("\n" + "="*65)
    print(f"{'Метод поиска в глубину (DFS) от вершины S':^65}")
    print("="*65)
    print(f"| {'Вершина':^8} | {'Путь (маршрут)':^30} | {'Расстояние':^12} |")
    print("-" * 65)
    
    # Для удобства выводим в порядке вершин
    order = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    for node in order:
        if node in results:
            path, dist = results[node]
            path_str = " -> ".join(path)
            if node == 'S':
                path_str = "S (старт)"
            print(f"| {node:^8} | {path_str:^30} | {dist:^12} |")
    print("="*65 + "\n")

# Запуск
if __name__ == "__main__":
    draw_graph()
    dfs_res = dfs_paths(G, 'S')
    print_dfs_table(dfs_res)
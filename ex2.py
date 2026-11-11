import networkx as nx
import matplotlib.pyplot as plt

# ==========================================
# 1. ВВОД ГРАФА (Матрица расстояний)
# ==========================================
# Вершины графа
nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

# Веса ребер (строго по вашим данным)
edges = [
    ('S', 'A', 1),
    ('S', 'C', 1),
    ('S', 'B', 1),  # B S 1
    ('C', 'F', 7),
    ('F', 'G', 6),
    ('D', 'G', 3),
    ('A', 'D', 2),
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
    
    # Фиксируем координаты вершин так же, как на Рис.2
    pos = {
        'S': (0.5, 1.0),
        'A': (0.2, 0.7), 'B': (0.5, 0.7), 'C': (0.8, 0.7),
        'D': (0.2, 0.3), 'E': (0.5, 0.3), 'F': (0.8, 0.3),
        'G': (0.5, 0.0)
    }
    
    # Рисуем вершины и ребра
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightgreen', 
            font_size=12, font_weight='bold', edge_color='black', width=2)
    
    # Подписываем веса (расстояния)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
    
    plt.title("Задание 2. Граф (Рис.2) с вашими весами")
    plt.axis('off')
    plt.show()

# ==========================================
# 3. АЛГОРИТМ DFS (Поиск в глубину)
# ==========================================
def dfs_paths(graph, start_node):
    # Стек: (вершина, путь_до_нее, суммарное_расстояние)
    stack = [(start_node, [start_node], 0)]
    visited = set()
    results = {}
    step_order = 1

    while stack:
        # Извлекаем последний добавленный элемент (LIFO)
        current_node, path, dist = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            
            # Сохраняем путь, расстояние и порядок посещения
            results[current_node] = (path, dist, step_order)
            step_order += 1

            # Получаем соседей
            neighbors = list(graph.neighbors(current_node))
            
            # ХИТРОСТЬ ДЛЯ СООТВЕТСТВИЯ РИС.2:
            # На рисунке обход идет влево (A, потом D...), поэтому 
            # сортируем соседей в обратном алфавитном порядке, 
            # чтобы первой в стек попала 'C' (правая), а последней 'A' (левая),
            # и алгоритм достал сначала 'A'.
            neighbors.sort(reverse=True)

            for neighbor in neighbors:
                if neighbor not in visited:
                    edge_weight = graph[current_node][neighbor]['weight']
                    new_dist = dist + edge_weight
                    new_path = path + [neighbor]
                    
                    # Добавляем в стек
                    stack.append((neighbor, new_path, new_dist))
                    
    return results

# ==========================================
# 4. ВЫВОД ТАБЛИЦЫ РЕЗУЛЬТАТОВ
# ==========================================
def print_dfs_table(results):
    print("\n" + "="*75)
    print(f"{'Метод поиска в глубину (DFS) от вершины S':^75}")
    print("="*75)
    print(f"| {'Порядок':^7} | {'Вершина':^8} | {'Путь (маршрут)':^32} | {'Расстояние':^10} |")
    print("-" * 75)
    
    # Сортируем по порядку посещения
    sorted_results = sorted(results.items(), key=lambda item: item[1][2])
    
    for node, (path, dist, step) in sorted_results:
        path_str = " -> ".join(path)
        if node == 'S':
            path_str = "S (старт)"
        print(f"| {step:^7} | {node:^8} | {path_str:^32} | {dist:^10} |")
    print("="*75 + "\n")

# Запускаем
if __name__ == "__main__":
    draw_graph()
    dfs_results = dfs_paths(G, 'S')
    print_dfs_table(dfs_results)
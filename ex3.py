import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# ==========================================
# 1. ВВОД ГРАФА (Матрица расстояний)
# ==========================================
# Вершины графа
nodes = [1, 2, 3, 4, 5]

# Все ребра единичные (вес = 1)
edges = [
    (1, 2, 1), (1, 5, 1),  # e1, e2
    (5, 2, 1),             # e3
    (5, 4, 1),             # e4
    (2, 3, 1),             # e5
    (4, 3, 1)              # e6, e7 (считаем как одну связь для матрицы)
]

# Создаем неориентированный граф
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# ==========================================
# 2. ВЫВОД РИСУНКА ГРАФА
# ==========================================
def draw_graph():
    plt.figure(figsize=(7, 7))
    
    # Координаты вершин в виде пятиугольника
    pos = {
        1: (0.5, 1.0),    # Верх
        2: (0.9, 0.6),    # Справа
        3: (0.7, 0.1),    # Низ-справа
        4: (0.3, 0.1),    # Низ-слева
        5: (0.1, 0.6)     # Слева
    }
    
    # Рисуем вершины и ребра
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightyellow', 
            font_size=14, font_weight='bold', edge_color='black', width=2)
    
    # Добавляем подписи ребер (e1, e2 и т.д.) для красоты
    edge_labels = {
        (1, 2): 'e2', (1, 5): 'e1',
        (5, 2): 'e3',
        (5, 4): 'e4',
        (2, 3): 'e5',
        (4, 3): 'e6/e7'
    }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue', font_size=10)
    
    plt.title("Задание 3. Пятиугольный граф (все ребра = 1)")
    plt.axis('off')
    plt.show()

# ==========================================
# 3. АЛГОРИТМЫ BFS и DFS
# ==========================================
def get_bfs_paths(graph, start):
    # BFS использует ОЧЕРЕДЬ (deque)
    queue = deque([(start, [start])])
    visited = set()
    results = {}
    
    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            results[node] = path
            for neighbor in sorted(graph.neighbors(node)): # сортируем для порядка
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return results

def get_dfs_paths(graph, start):
    # DFS использует СТЕК (list)
    stack = [(start, [start])]
    visited = set()
    results = {}
    
    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            results[node] = path
            # Для DFS добавляем соседей в обратном порядке (чтобы меньшие номера посещались первыми)
            for neighbor in sorted(graph.neighbors(node), reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return results

# ==========================================
# 4. ВЫВОД ТАБЛИЦЫ СРАВНЕНИЯ
# ==========================================
def print_comparison_table(bfs_res, dfs_res):
    print("\n" + "="*75)
    print(f"{'Таблица сравнения путей от вершины 1 (BFS vs DFS)':^75}")
    print("="*75)
    print(f"| {'Вершина':^7} | {'Путь BFS (в ширину)':^25} | {'Путь DFS (в глубину)':^25} |")
    print("-" * 75)
    
    for node in [1, 2, 3, 4, 5]:
        if node in bfs_res and node in dfs_res:
            bfs_str = " -> ".join(map(str, bfs_res[node]))
            dfs_str = " -> ".join(map(str, dfs_res[node]))
            if node == 1:
                bfs_str = "1 (старт)"
                dfs_str = "1 (старт)"
            print(f"| {node:^7} | {bfs_str:^25} | {dfs_str:^25} |")
    print("="*75 + "\n")

# Запускаем программу
if __name__ == "__main__":
    draw_graph()
    
    bfs_results = get_bfs_paths(G, 1)
    dfs_results = get_dfs_paths(G, 1)
    
    print_comparison_table(bfs_results, dfs_results)
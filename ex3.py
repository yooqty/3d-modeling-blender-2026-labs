import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# ==========================================
# 1. ВВОД ГРАФА (Матрица расстояний)
# ==========================================
nodes = [1, 2, 3, 4, 5]

# Все ребра имеют вес 1
edges = [
    (1, 2, 1), (1, 5, 1),  # e2, e1
    (5, 2, 1),             # e3
    (5, 4, 1),             # e4
    (2, 3, 1),             # e5
    (4, 3, 1)              # e6, e7
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# ==========================================
# 2. ВЫВОД РИСУНКА ГРАФА
# ==========================================
def draw_graph():
    plt.figure(figsize=(7, 7))
    
    # Координаты для красивого пятиугольника
    pos = {
        1: (0.5, 1.0),
        2: (0.9, 0.6),
        3: (0.7, 0.1),
        4: (0.3, 0.1),
        5: (0.1, 0.6)
    }
    
    nx.draw(G, pos, with_labels=True, node_size=900, node_color='lightcyan', 
            font_size=14, font_weight='bold', edge_color='black', width=2)
    
    # Подписи ребер (все расстояния = 1)
    edge_labels = {(u, v): '1' for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
    
    plt.title("Задание 3. Граф (все ребра = 1)")
    plt.axis('off')
    plt.show()

# ==========================================
# 3. АЛГОРИТМЫ BFS и DFS
# ==========================================
def get_bfs_paths(graph, start):
    queue = deque([(start, [start], 0)])
    visited = set()
    results = {}
    
    while queue:
        node, path, dist = queue.popleft()
        if node not in visited:
            visited.add(node)
            results[node] = (path, dist)
            for neighbor in sorted(graph.neighbors(node)):
                if neighbor not in visited:
                    weight = graph[node][neighbor]['weight']
                    queue.append((neighbor, path + [neighbor], dist + weight))
    return results

def get_dfs_paths(graph, start):
    stack = [(start, [start], 0)]
    visited = set()
    results = {}
    
    while stack:
        node, path, dist = stack.pop()
        if node not in visited:
            visited.add(node)
            results[node] = (path, dist)
            for neighbor in sorted(graph.neighbors(node), reverse=True):
                if neighbor not in visited:
                    weight = graph[node][neighbor]['weight']
                    stack.append((neighbor, path + [neighbor], dist + weight))
    return results

# ==========================================
# 4. ВЫВОД ТАБЛИЦЫ СРАВНЕНИЯ
# ==========================================
def print_comparison_table(bfs_res, dfs_res):
    print("\n" + "="*85)
    print(f"{'Таблица сравнения путей от вершины 1 (BFS vs DFS)':^85}")
    print("="*85)
    print(f"| {'Вершина':^7} | {'Путь BFS':^22} | {'Расст. BFS':^10} | {'Путь DFS':^22} | {'Расст. DFS':^10} |")
    print("-" * 85)
    
    for node in [1, 2, 3, 4, 5]:
        if node in bfs_res and node in dfs_res:
            bfs_path, bfs_dist = bfs_res[node]
            dfs_path, dfs_dist = dfs_res[node]
            
            bfs_str = " -> ".join(map(str, bfs_path))
            dfs_str = " -> ".join(map(str, dfs_path))
            
            if node == 1:
                bfs_str = "1 (старт)"
                dfs_str = "1 (старт)"
                
            print(f"| {node:^7} | {bfs_str:^22} | {bfs_dist:^10} | {dfs_str:^22} | {dfs_dist:^10} |")
    print("="*85 + "\n")

# Запуск
if __name__ == "__main__":
    draw_graph()
    bfs_results = get_bfs_paths(G, 1)
    dfs_results = get_dfs_paths(G, 1)
    print_comparison_table(bfs_results, dfs_results)